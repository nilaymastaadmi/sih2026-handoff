"""
PS 26169 feasibility spike, 2026-09-01.

Purpose: decide whether ISRO's five published performance targets are reachable,
and whether the swappable-frame-source architecture holds up. This is a decision
artifact, not the competition entry.

Targets from the official PS 26169 annexure:
    acquisition time      <= 2 s
    tracking error        <= 10 px
    target loss           <  5 %
    re-acquisition time   <= 1 s
    processing speed      >= 20 FPS

Annexure disturbance limits exercised here:
    salt and pepper ~10% of image, Gaussian, Poisson
    noise standard deviation up to 20
    camera jitter up to +/- 20 px/frame
    platform motion up to +/- 20 px/frame
    atmospheric conditions: clear, haze, fog, rain, low light

Dependencies: numpy only.
"""

import math
import time
from dataclasses import dataclass, field

import numpy as np

# ----------------------------------------------------------------------------
# Geometry. Annexure: 640x480 sensor, default FOV 4 deg x 3 deg.
# ----------------------------------------------------------------------------
W, H = 640, 480
FOV_X_DEG = 4.0
DEG_PER_PX = FOV_X_DEG / W          # 0.00625 deg/px
URAD_PER_PX = math.radians(DEG_PER_PX) * 1e6   # ~109 urad/px
FPS_NOMINAL = 30.0
DT = 1.0 / FPS_NOMINAL
MAX_SLEW_DEG_S = 5.0                # annexure allows 5 to 10; use the tight end
GIMBAL_LIMIT_DEG = 2.5              # travel limit; scene spans about +/-1.6 deg

ATMOSPHERE = {
    # name: (contrast_gain, brightness_offset, extra_blur_sigma_px)
    "clear":    (1.00, 0.0, 0.8),
    "haze":     (0.70, 12.0, 1.4),
    "fog":      (0.45, 25.0, 2.2),
    "rain":     (0.60, 8.0, 1.8),
    "lowlight": (0.35, -5.0, 1.0),
}


@dataclass
class Scenario:
    name: str
    motion: str = "circular"        # straight | circular | figure8 | random
    atmosphere: str = "clear"
    noise_sigma: float = 6.0        # annexure max 20
    salt_pepper: float = 0.0        # fraction of image, annexure ~0.10
    poisson: bool = False
    jitter_px: float = 0.0          # camera jitter, annexure max 20 px/frame
    platform_px: float = 0.0        # platform motion, annexure max 20 px/frame
    spot_px: float = 10.0           # annexure default 10x10, range 5-20
    duration_s: float = 20.0
    induce_loss_at_s: float = 10.0  # force an occlusion to measure re-acquisition
    seed: int = 0


# ----------------------------------------------------------------------------
# Beacon truth, in world angular coordinates (degrees).
# ----------------------------------------------------------------------------
def beacon_truth(t, motion, rng_state):
    """Return (az_deg, el_deg) of the beacon at time t."""
    amp = 1.2
    if motion == "straight":
        return (-1.5 + 0.15 * t, 0.35 * math.sin(0.05 * t))
    if motion == "circular":
        w = 2 * math.pi / 12.0
        return (amp * math.cos(w * t), 0.7 * amp * math.sin(w * t))
    if motion == "figure8":
        w = 2 * math.pi / 14.0
        return (amp * math.sin(w * t), 0.7 * amp * math.sin(2 * w * t))
    if motion == "random":
        # smooth random walk, deterministic in t via the supplied state
        az, el = rng_state["az"], rng_state["el"]
        rng = rng_state["rng"]
        rng_state["vaz"] = 0.90 * rng_state["vaz"] + rng.normal(0, 0.035)
        rng_state["vel"] = 0.90 * rng_state["vel"] + rng.normal(0, 0.030)
        az = max(-1.6, min(1.6, az + rng_state["vaz"]))
        el = max(-1.1, min(1.1, el + rng_state["vel"]))
        rng_state["az"], rng_state["el"] = az, el
        return (az, el)
    raise ValueError(motion)


# ----------------------------------------------------------------------------
# Frame sources. The swappable interface is the whole point: Benchmark
# Performance-2 requires bypassing the internal camera and ingesting external
# video, and that cannot be retrofitted late.
# ----------------------------------------------------------------------------
class FrameSource:
    #: A live/simulated camera responds to pan and tilt, so the pointing loop can
    #: be closed around it. Pre-recorded video does not: its viewpoint is fixed.
    #: Benchmark Performance-2 supplies .mp4 files, so that path must run
    #: open-loop and report centroiding error only. Closing a loop around a
    #: recording produces permanent controller saturation and a meaningless score.
    steerable = True

    def frame(self, t, pan, tilt):
        raise NotImplementedError

    def truth(self, t):
        """Optional ground truth in pixels, or None when unknown (real video)."""
        return None


class SceneFrameSource(FrameSource):
    """Synthetic scene: sub-pixel Gaussian beacon plus the annexure disturbances."""

    def __init__(self, sc: Scenario):
        self.sc = sc
        self.rng = np.random.default_rng(sc.seed)
        self._rs = {"az": 0.0, "el": 0.0, "vaz": 0.0, "vel": 0.0,
                    "rng": np.random.default_rng(sc.seed + 1)}
        self._last_truth_px = None
        yy, xx = np.mgrid[0:H, 0:W]
        self._xx = xx.astype(np.float32)
        self._yy = yy.astype(np.float32)

    def _world_to_px(self, az, el, pan, tilt):
        x = (az - pan) / DEG_PER_PX + W / 2.0
        y = (el - tilt) / DEG_PER_PX + H / 2.0
        return x, y

    def frame(self, t, pan, tilt):
        sc = self.sc
        az, el = beacon_truth(t, sc.motion, self._rs)

        # angle-of-arrival jitter (beam wander) plus platform motion, in pixels
        jit_x = self.rng.normal(0, sc.jitter_px / 3.0) if sc.jitter_px else 0.0
        jit_y = self.rng.normal(0, sc.jitter_px / 3.0) if sc.jitter_px else 0.0
        plat_x = sc.platform_px * math.sin(2 * math.pi * 0.8 * t) if sc.platform_px else 0.0
        plat_y = sc.platform_px * math.cos(2 * math.pi * 0.6 * t) if sc.platform_px else 0.0

        cx, cy = self._world_to_px(az, el, pan, tilt)
        cx += jit_x + plat_x
        cy += jit_y + plat_y
        self._last_truth_px = (cx, cy)

        gain, offset, blur = ATMOSPHERE[sc.atmosphere]
        sigma = max(0.7, sc.spot_px / 4.0) + blur

        img = np.full((H, W), 18.0, dtype=np.float32)          # sky background
        # render the beacon only in a local window, for speed
        x0, x1 = int(max(0, cx - 6 * sigma)), int(min(W, cx + 6 * sigma + 1))
        y0, y1 = int(max(0, cy - 6 * sigma)), int(min(H, cy + 6 * sigma + 1))
        occluded = abs(t - sc.induce_loss_at_s) < 0.45      # forced dropout
        if x1 > x0 and y1 > y0 and not occluded:
            sx = self._xx[y0:y1, x0:x1] - cx
            sy = self._yy[y0:y1, x0:x1] - cy
            peak = 210.0
            img[y0:y1, x0:x1] += peak * np.exp(-(sx * sx + sy * sy) / (2 * sigma * sigma))

        # atmosphere: contrast and brightness, per the annexure description
        img = img * gain + offset

        if sc.poisson:
            img = self.rng.poisson(np.clip(img, 0, None)).astype(np.float32)
        if sc.noise_sigma:
            img += self.rng.normal(0, sc.noise_sigma, img.shape).astype(np.float32)
        if sc.salt_pepper:
            n = int(sc.salt_pepper * img.size)
            idx = self.rng.integers(0, img.size, n)
            flat = img.reshape(-1)
            half = n // 2
            flat[idx[:half]] = 255.0
            flat[idx[half:]] = 0.0

        return np.clip(img, 0, 255).astype(np.uint8)

    def truth(self, t):
        return self._last_truth_px


class ArrayFrameSource(FrameSource):
    """Ingests pre-rendered frames, standing in for ISRO's supplied .mp4.

    This exists to prove the interface: the tracker is never told which source
    it is reading from.
    """

    steerable = False

    def __init__(self, frames, truths=None):
        self.frames = frames
        self.truths = truths
        self._i = 0
        self._t = None

    def frame(self, t, pan, tilt):
        self._i = min(int(round(t * FPS_NOMINAL)), len(self.frames) - 1)
        self._t = t
        return self.frames[self._i]

    def truth(self, t):
        if self.truths is None:
            return None
        return self.truths[self._i]


# ----------------------------------------------------------------------------
# Detection: background estimate, adaptive threshold, windowed centre of gravity.
# ----------------------------------------------------------------------------
class Detector:
    """Median-MAD threshold, 3x3 box smoothing to suppress impulse noise, then a
    windowed centre of gravity. When the tracker is locked the search is confined
    to a region of interest around the prediction, which is what stops a
    salt-and-pepper spike at the frame edge from capturing the track."""

    def __init__(self, k=6.0, win=9):
        self.k = k
        self.win = win

    def detect(self, img, predict=None, roi=70):
        f = img.astype(np.float32)
        med = float(np.median(f))
        mad = float(np.median(np.abs(f - med))) + 1e-6
        sigma = 1.4826 * mad

        acc = np.zeros_like(f)
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                acc += np.roll(np.roll(f, dy, axis=0), dx, axis=1)
        sm = acc / 9.0
        # box smoothing divides the noise standard deviation by 3
        thr = med + self.k * (sigma / 3.0)

        if predict is not None:
            px, py = predict
            rx0, rx1 = int(max(0, px - roi)), int(min(W, px + roi + 1))
            ry0, ry1 = int(max(0, py - roi)), int(min(H, py + roi + 1))
            if rx1 - rx0 < 3 or ry1 - ry0 < 3:
                return None
            sub = sm[ry0:ry1, rx0:rx1]
            jy, jx = np.unravel_index(int(np.argmax(sub)), sub.shape)
            iy, ix = jy + ry0, jx + rx0
        else:
            iy, ix = np.unravel_index(int(np.argmax(sm)), sm.shape)

        if sm[iy, ix] < thr:
            return None

        w = self.win
        y0, y1 = max(0, iy - w), min(H, iy + w + 1)
        x0, x1 = max(0, ix - w), min(W, ix + w + 1)
        patch = sm[y0:y1, x0:x1] - med
        patch = np.clip(patch, 0, None)
        tot = float(patch.sum())
        if tot <= 1e-6:
            return None
        yy, xx = np.mgrid[y0:y1, x0:x1]
        cx = float((patch * xx).sum() / tot)
        cy = float((patch * yy).sum() / tot)
        snr = (float(sm[iy, ix]) - med) / (sigma / 3.0)
        return cx, cy, snr


# ----------------------------------------------------------------------------
# Constant-velocity Kalman filter with innovation gating.
# ----------------------------------------------------------------------------
class Tracker:
    """Constant-velocity Kalman filter with innovation gating, filtering in a
    camera-compensated frame. ego_shift() removes the known pan/tilt motion so the
    filter models target motion only and does not fight the control loop.
    Lock requires CONFIRM consecutive accepted measurements, so a single noise
    spike cannot declare acquisition."""

    CONFIRM = 3
    SNR_FLOOR = 5.0

    def __init__(self, dt=DT, q=900.0, gate_chi2=13.8):   # chi2, 2 dof, ~99.9%
        self.dt = dt
        # constant-acceleration model: a constant-velocity filter lags badly on
        # curved trajectories, which is the figure-of-eight and circular cases
        self.F = np.array([
            [1, 0, dt, 0, 0.5 * dt * dt, 0],
            [0, 1, 0, dt, 0, 0.5 * dt * dt],
            [0, 0, 1, 0, dt, 0],
            [0, 0, 0, 1, 0, dt],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1]], float)
        self.H = np.array([[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0]], float)
        g = np.array([[dt * dt / 2, 0], [0, dt * dt / 2],
                      [dt, 0], [0, dt], [1.0, 0], [0, 1.0]], float)
        self.Q = g @ g.T * q
        self.gate = gate_chi2
        self.n = 6
        self.x = None
        self.P = None
        self.locked = False
        self.miss = 0
        self.hits = 0

    def ego_shift(self, dpan_deg, dtilt_deg):
        """The camera moved, so every image-plane position shifts by the negative
        of that motion. Applying it to the state keeps the filter in a frame where
        the target moves smoothly."""
        if self.x is None:
            return
        self.x[0] -= dpan_deg / DEG_PER_PX
        self.x[1] -= dtilt_deg / DEG_PER_PX

    def start(self, z):
        self.x = np.array([z[0], z[1], 0.0, 0.0, 0.0, 0.0], float)
        self.P = np.diag([25.0, 25.0, 400.0, 400.0, 2500.0, 2500.0])
        self.locked = False
        self.miss = 0
        self.hits = 1

    def step(self, z, snr):
        # a detection too weak to be a beacon is not a detection; without this
        # floor the filter locks onto noise and drags the camera off target
        if z is not None and snr < self.SNR_FLOOR:
            z = None
        if self.x is None:
            if z is not None:
                self.start(z)
            return
        self.x = self.F @ self.x
        self.P = self.F @ self.P @ self.F.T + self.Q

        if z is None:
            self.miss += 1
            self.hits = 0
            if self.miss > 5:            # coast a few frames before declaring loss
                self.locked = False
                if self.miss > 20:       # give up and allow a full-frame re-search
                    self.x = None
            return

        r = max(1.0, 400.0 / max(snr, 1.0))     # measurement noise from SNR
        R = np.diag([r, r])
        y = np.array([z[0], z[1]], float) - self.H @ self.x
        S = self.H @ self.P @ self.H.T + R
        try:
            Sinv = np.linalg.inv(S)
        except np.linalg.LinAlgError:
            return
        nis = float(y @ Sinv @ y)
        if self.locked and nis > self.gate:
            self.miss += 1                       # reject the outlier, keep coasting
            if self.miss > 5:
                self.locked = False
            return
        K = self.P @ self.H.T @ Sinv
        self.x = self.x + K @ y
        self.P = (np.eye(self.n) - K @ self.H) @ self.P
        self.miss = 0
        self.hits += 1
        if self.hits >= self.CONFIRM:
            self.locked = True

    @property
    def pos(self):
        return None if self.x is None else (self.x[0], self.x[1])


# ----------------------------------------------------------------------------
# Pan/tilt controller with an explicit slew-rate limit.
# ----------------------------------------------------------------------------
class Controller:
    def __init__(self, kp=0.55, ki=0.05, max_slew=MAX_SLEW_DEG_S):
        self.kp, self.ki = kp, ki
        self.ix = self.iy = 0.0
        self.max_step = max_slew * DT       # degrees per frame
        self.saturated_frames = 0

    def update(self, err_px_x, err_px_y):
        ex = err_px_x * DEG_PER_PX
        ey = err_px_y * DEG_PER_PX
        self.ix = max(-0.5, min(0.5, self.ix + ex * DT))
        self.iy = max(-0.5, min(0.5, self.iy + ey * DT))
        dpan = self.kp * ex + self.ki * self.ix
        dtilt = self.kp * ey + self.ki * self.iy
        mag = math.hypot(dpan, dtilt)
        if mag > self.max_step:
            dpan *= self.max_step / mag
            dtilt *= self.max_step / mag
            self.saturated_frames += 1
        return dpan, dtilt


# ----------------------------------------------------------------------------
# Scenario runner. Emits exactly the annexure's performance-log fields.
# ----------------------------------------------------------------------------
def run(sc: Scenario, source: FrameSource = None, verbose=False):
    src = source if source is not None else SceneFrameSource(sc)
    det = Detector()
    trk = Tracker()
    ctl = Controller()

    pan = tilt = 0.0
    n = int(sc.duration_s * FPS_NOMINAL)
    errs = []
    locked_frames = 0
    acq_time = None
    reacq_time = None
    loss_started = None
    was_locked = False
    t_compute = 0.0

    for i in range(n):
        t = i * DT
        img = src.frame(t, pan, tilt)

        t0 = time.perf_counter()
        pred = trk.pos if trk.locked else None
        d = det.detect(img, predict=pred)
        z = (d[0], d[1]) if d else None
        snr = d[2] if d else 0.0
        trk.step(z, snr)
        t_compute += time.perf_counter() - t0

        if trk.locked and acq_time is None:
            acq_time = t
        if was_locked and not trk.locked:
            loss_started = t
        if (not was_locked) and trk.locked and loss_started is not None and reacq_time is None:
            reacq_time = t - loss_started
        was_locked = trk.locked

        if trk.locked:
            locked_frames += 1
            gt = src.truth(t)
            if gt is not None:
                px, py = trk.pos
                errs.append(math.hypot(px - gt[0], py - gt[1]))
        if trk.locked and src.steerable:
            ex = trk.pos[0] - W / 2.0
            ey = trk.pos[1] - H / 2.0
            dpan, dtilt = ctl.update(ex, ey)
            # a real gimbal has travel limits; without them a bad lock walks the
            # camera off the sky and the run never recovers
            new_pan = max(-GIMBAL_LIMIT_DEG, min(GIMBAL_LIMIT_DEG, pan + dpan))
            new_tilt = max(-GIMBAL_LIMIT_DEG, min(GIMBAL_LIMIT_DEG, tilt + dtilt))
            dpan, dtilt = new_pan - pan, new_tilt - tilt
            pan, tilt = new_pan, new_tilt
            # the filter lives in a camera-compensated frame, so remove the
            # motion we just commanded instead of letting it look like target motion
            trk.ego_shift(dpan, dtilt)

    errs = np.array(errs) if errs else np.array([np.nan])
    fps = n / t_compute if t_compute > 0 else float("inf")
    return {
        "scenario": sc.name,
        "frames": n,
        "acq_s": acq_time,
        "reacq_s": reacq_time,
        "err_mean_px": float(np.nanmean(errs)),
        "err_max_px": float(np.nanmax(errs)),
        "err_p95_px": float(np.nanpercentile(errs, 95)),
        "loss_pct": 100.0 * (1.0 - locked_frames / n),
        "fps": fps,
        "sat_pct": 100.0 * ctl.saturated_frames / max(1, locked_frames),
    }


TARGETS = {"acq_s": 2.0, "err_mean_px": 10.0, "loss_pct": 5.0, "reacq_s": 1.0, "fps": 20.0}


def verdict(r):
    ok = []
    ok.append(r["acq_s"] is not None and r["acq_s"] <= TARGETS["acq_s"])
    ok.append(r["err_mean_px"] <= TARGETS["err_mean_px"])
    ok.append(r["loss_pct"] < TARGETS["loss_pct"])
    ok.append(r["reacq_s"] is None or r["reacq_s"] <= TARGETS["reacq_s"])
    ok.append(r["fps"] >= TARGETS["fps"])
    return sum(ok), len(ok)


def fmt(r):
    a = f"{r['acq_s']:.2f}" if r["acq_s"] is not None else "none"
    ra = f"{r['reacq_s']:.2f}" if r["reacq_s"] is not None else "-"
    p, q = verdict(r)
    return (f"{r['scenario']:<34} acq {a:>5}s  err {r['err_mean_px']:>6.2f}px "
            f"(p95 {r['err_p95_px']:>6.2f}, max {r['err_max_px']:>7.2f})  "
            f"loss {r['loss_pct']:>5.2f}%  reacq {ra:>5}s  {r['fps']:>6.1f} FPS  "
            f"sat {r['sat_pct']:>5.1f}%   [{p}/{q}]")


def main():
    print("PS 26169 feasibility spike")
    print(f"geometry: {W}x{H}, FOV {FOV_X_DEG} deg, {DEG_PER_PX:.5f} deg/px = "
          f"{URAD_PER_PX:.1f} urad/px, so the 10 px target = "
          f"{10*URAD_PER_PX/1000:.2f} mrad")
    print(f"slew cap {MAX_SLEW_DEG_S} deg/s = {MAX_SLEW_DEG_S*DT/DEG_PER_PX:.1f} px/frame "
          f"of correction authority at {FPS_NOMINAL:.0f} fps")
    print("targets: acq <=2s, err <=10px, loss <5%, reacq <=1s, fps >=20")
    print("-" * 132)

    scenarios = [
        Scenario("baseline clear circular", motion="circular"),
        Scenario("straight line, haze", motion="straight", atmosphere="haze", noise_sigma=10),
        Scenario("figure8, rain", motion="figure8", atmosphere="rain", noise_sigma=12),
        Scenario("random walk, lowlight", motion="random", atmosphere="lowlight", noise_sigma=10),
        Scenario("fog + poisson", motion="circular", atmosphere="fog", noise_sigma=14, poisson=True),
        Scenario("salt&pepper 10% (annexure max)", motion="circular", salt_pepper=0.10, noise_sigma=8),
        Scenario("jitter 20px/frame (max)", motion="circular", jitter_px=20.0, noise_sigma=8),
        Scenario("platform 20px/frame (max)", motion="circular", platform_px=20.0, noise_sigma=8),
        Scenario("small spot 5px", motion="circular", spot_px=5.0, noise_sigma=8),
        Scenario("large spot 20px", motion="circular", spot_px=20.0, noise_sigma=8),
        Scenario("WORST CASE all-max", motion="random", atmosphere="fog", noise_sigma=20,
                 salt_pepper=0.10, poisson=True, jitter_px=20.0, platform_px=20.0, spot_px=8.0),
    ]

    results = []
    for sc in scenarios:
        r = run(sc)
        results.append(r)
        print(fmt(r))

    print("-" * 132)
    passed = sum(1 for r in results if verdict(r)[0] == verdict(r)[1])
    print(f"scenarios meeting all 5 published targets: {passed} of {len(results)}")

    # ---- prove the swappable frame source, which is 30% of the marks ----
    print()
    print("Benchmark Performance-2 rehearsal: same tracker, external frame source")
    sc = Scenario("prerendered handoff", motion="figure8", atmosphere="haze",
                  noise_sigma=10, seed=7)
    gen = SceneFrameSource(sc)
    frames, truths = [], []
    pan = tilt = 0.0
    for i in range(int(sc.duration_s * FPS_NOMINAL)):
        t = i * DT
        frames.append(gen.frame(t, pan, tilt))
        truths.append(gen.truth(t))
    r2 = run(sc, source=ArrayFrameSource(frames, truths))
    print(fmt(r2))
    print("tracker consumed externally supplied frames with no change to detect/track/log.")


if __name__ == "__main__":
    main()
