"""Full-screen acquisition test for PS 26169.

The annexure specifies a screen of minimum 2000x2000 px with the camera starting
at its centre and the target's initial location random. The 640x480 sensor at
4x3 deg sees ~1/13 of that world, so acquisition is a search problem, not a
detection-latency problem. fsoc_spike.py's scenario scenes span +/-1.6 deg and
never exercise the search; this script does.

Method: beacon spawns uniformly on the 2000x2000 screen (+/-6.25 deg at the
spike's 0.00625 deg/px), drifts on a slow straight line. The camera runs an
expanding-square tile search at the 5 deg/s slew cap using the spike's own
Detector and Tracker (lock = 3 consecutive confirmed hits, SNR-floored).
Acquisition time = first lock. N seeded runs -> CDF.

Output: acquisition_cdf.json, acquisition_cdf.png, and a console summary.
Dependencies: numpy, PIL; matplotlib used for the plot if present.
"""

import json
import math

import numpy as np

from fsoc_spike import (W, H, DEG_PER_PX, DT, FPS_NOMINAL, MAX_SLEW_DEG_S,
                        Detector, Tracker, Controller)

SCREEN_PX = 2000                       # annexure minimum, square
HALF_DEG = SCREEN_PX / 2 * DEG_PER_PX  # 6.25 deg half-extent
FOV_X = W * DEG_PER_PX                 # 4.0
FOV_Y = H * DEG_PER_PX                 # 3.0
TILE_X = FOV_X * 0.85                  # 15% overlap between visited tiles
TILE_Y = FOV_Y * 0.85
MAX_STEP = MAX_SLEW_DEG_S * DT         # deg per frame at the cap
TIMEOUT_S = 25.0
SPAWN_MARGIN_DEG = 0.15                # keep the spot fully on the screen
TARGET_S = 2.0                         # the annexure's acquisition target


class WideScene:
    """The spike's scene render, on the full annexure screen."""

    def __init__(self, seed, noise_sigma=6.0, spot_px=10.0):
        self.rng = np.random.default_rng(seed)
        lim = HALF_DEG - SPAWN_MARGIN_DEG
        self.az0 = float(self.rng.uniform(-lim, lim))
        self.el0 = float(self.rng.uniform(-lim, lim))
        ang = float(self.rng.uniform(0, 2 * math.pi))
        speed = 0.15                    # deg/s, the spike's straight-line rate
        self.vaz = speed * math.cos(ang)
        self.vel = speed * math.sin(ang)
        self.noise_sigma = noise_sigma
        self.sigma = max(0.7, spot_px / 4.0) + 0.8   # clear-atmosphere blur
        yy, xx = np.mgrid[0:H, 0:W]
        self._xx = xx.astype(np.float32)
        self._yy = yy.astype(np.float32)
        self.last_truth = None

    def beacon(self, t):
        lim = HALF_DEG - SPAWN_MARGIN_DEG
        az = self.az0 + self.vaz * t
        el = self.el0 + self.vel * t
        # reflect at the screen edge so the target stays on screen
        az = lim - abs((az + lim) % (4 * lim) - 2 * lim) if abs(az) > lim else az
        el = lim - abs((el + lim) % (4 * lim) - 2 * lim) if abs(el) > lim else el
        return az, el

    def frame(self, t, pan, tilt):
        az, el = self.beacon(t)
        cx = (az - pan) / DEG_PER_PX + W / 2.0
        cy = (el - tilt) / DEG_PER_PX + H / 2.0
        self.last_truth = (cx, cy)
        img = np.full((H, W), 18.0, dtype=np.float32)
        s = self.sigma
        x0, x1 = int(max(0, cx - 6 * s)), int(min(W, cx + 6 * s + 1))
        y0, y1 = int(max(0, cy - 6 * s)), int(min(H, cy + 6 * s + 1))
        if x1 > x0 and y1 > y0:
            sx = self._xx[y0:y1, x0:x1] - cx
            sy = self._yy[y0:y1, x0:x1] - cy
            img[y0:y1, x0:x1] += 210.0 * np.exp(-(sx * sx + sy * sy) / (2 * s * s))
        img += self.rng.normal(0, self.noise_sigma, img.shape).astype(np.float32)
        return np.clip(img, 0, 255).astype(np.uint8)


def search_waypoints():
    """Expanding-square tile centres covering the screen, centre first."""
    nx = math.ceil((2 * HALF_DEG) / TILE_X)
    ny = math.ceil((2 * HALF_DEG) / TILE_Y)
    pts = []
    for iy in range(-(ny // 2), ny // 2 + 1):
        for ix in range(-(nx // 2), nx // 2 + 1):
            pts.append((ix * TILE_X, iy * TILE_Y, max(abs(ix), abs(iy))))
    # ring order; within a ring, sweep by angle for a contiguous path
    pts.sort(key=lambda p: (p[2], math.atan2(p[1], p[0])))
    return [(p[0], p[1]) for p in pts]


WAYPOINTS = search_waypoints()


def run_one(seed):
    scene = WideScene(seed)
    det = Detector()
    trk = Tracker()
    ctl = Controller()
    pan = tilt = 0.0
    wp = 0
    n = int(TIMEOUT_S * FPS_NOMINAL)
    started_in_fov = (abs(scene.az0) <= FOV_X / 2) and (abs(scene.el0) <= FOV_Y / 2)

    for i in range(n):
        t = i * DT
        img = scene.frame(t, pan, tilt)
        pred = trk.pos if trk.locked else None
        d = det.detect(img, predict=pred)
        z = (d[0], d[1]) if d else None
        snr = d[2] if d else 0.0
        trk.step(z, snr)
        if trk.locked:
            return t, started_in_fov

        if trk.x is not None:
            # a candidate exists: centre it under closed-loop control
            ex = trk.x[0] - W / 2.0
            ey = trk.x[1] - H / 2.0
            dpan, dtilt = ctl.update(ex, ey)
        else:
            # blind search: slew toward the current waypoint at the cap
            tx, ty = WAYPOINTS[wp]
            dx, dy = tx - pan, ty - tilt
            dist = math.hypot(dx, dy)
            if dist < 0.05:
                wp = (wp + 1) % len(WAYPOINTS)
                dpan = dtilt = 0.0
            else:
                step = min(MAX_STEP, dist)
                dpan, dtilt = step * dx / dist, step * dy / dist
        pan = max(-HALF_DEG, min(HALF_DEG, pan + dpan))
        tilt = max(-HALF_DEG, min(HALF_DEG, tilt + dtilt))
        trk.ego_shift(dpan, dtilt)
    return None, started_in_fov


def main(n_runs=500):
    times, fails, in_fov_times, out_fov_times = [], 0, [], []
    for seed in range(n_runs):
        t, in_fov = run_one(seed)
        if t is None:
            fails += 1
        else:
            times.append(t)
            (in_fov_times if in_fov else out_fov_times).append(t)
        if (seed + 1) % 50 == 0:
            print(f"  {seed + 1}/{n_runs} done, {fails} timeouts so far", flush=True)

    a = np.array(sorted(times))
    within = float((a <= TARGET_S).mean() * len(a) / n_runs) if len(a) else 0.0
    summary = {
        "runs": n_runs,
        "screen_px": SCREEN_PX,
        "screen_deg": round(2 * HALF_DEG, 2),
        "slew_cap_deg_s": MAX_SLEW_DEG_S,
        "search": "expanding square, 15% tile overlap",
        "acquired": len(a),
        "timeouts_over_25s": fails,
        "fraction_within_2s": round(within, 4),
        "median_s": round(float(np.median(a)), 3) if len(a) else None,
        "p90_s": round(float(np.percentile(a, 90)), 3) if len(a) else None,
        "p95_s": round(float(np.percentile(a, 95)), 3) if len(a) else None,
        "max_s": round(float(a.max()), 3) if len(a) else None,
        "spawn_in_initial_fov": {
            "runs": len(in_fov_times),
            "median_s": round(float(np.median(in_fov_times)), 3) if in_fov_times else None,
        },
        "spawn_outside_initial_fov": {
            "runs": len(out_fov_times),
            "median_s": round(float(np.median(out_fov_times)), 3) if out_fov_times else None,
        },
    }
    with open("acquisition_cdf.json", "w") as f:
        json.dump({"summary": summary, "times_s": [round(float(x), 3) for x in a]}, f, indent=1)

    print("\nfull-screen acquisition, %d runs" % n_runs)
    for k, v in summary.items():
        print(f"  {k}: {v}")

    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        y = np.arange(1, len(a) + 1) / n_runs
        fig, ax = plt.subplots(figsize=(6, 3.6), dpi=160)
        ax.step(a, y, where="post", lw=2)
        ax.axvline(TARGET_S, ls="--", lw=1)
        ax.annotate(f"2 s target\n{within * 100:.0f}% acquired", (TARGET_S, 0.05),
                    xytext=(TARGET_S + 0.6, 0.08), fontsize=8)
        ax.set_xlabel("acquisition time (s)")
        ax.set_ylabel("fraction of 500 random spawns")
        ax.set_title("Full-screen acquisition CDF, 2000x2000 px, expanding-square search")
        ax.set_ylim(0, 1.02)
        ax.grid(alpha=0.3)
        fig.tight_layout()
        fig.savefig("acquisition_cdf.png")
        print("wrote acquisition_cdf.png")
    except Exception as e:  # matplotlib absent: numbers still stand
        print(f"plot skipped ({e}); acquisition_cdf.json carries the data")


if __name__ == "__main__":
    main()
