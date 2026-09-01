"""Produce the evidence artifacts for PS 26169:

  evidence_panels.png    tracked beacon under four disturbance regimes
  performance_log.json   the annexure's required auto-generated performance report

Run after fsoc_spike.py. numpy + PIL only.
"""

import json
import math

import numpy as np
from PIL import Image, ImageDraw

from fsoc_spike import (W, H, DT, FPS_NOMINAL, DEG_PER_PX, URAD_PER_PX,
                        GIMBAL_LIMIT_DEG, MAX_SLEW_DEG_S, Scenario,
                        SceneFrameSource, ArrayFrameSource, Detector, Tracker,
                        Controller, run, TARGETS, verdict)

PANELS = [
    ("clear", Scenario("clear", motion="circular", noise_sigma=6, seed=3)),
    ("fog + poisson", Scenario("fog", motion="circular", atmosphere="fog",
                               noise_sigma=14, poisson=True, seed=3)),
    ("salt & pepper 10%", Scenario("sp", motion="circular", salt_pepper=0.10,
                                   noise_sigma=8, seed=3)),
    ("worst case, all maxima", Scenario("worst", motion="random", atmosphere="fog",
                                        noise_sigma=20, salt_pepper=0.10, poisson=True,
                                        jitter_px=20, platform_px=20, spot_px=8, seed=3)),
]

GRAB_T = 6.0     # seconds into the run, well past acquisition


def grab(sc):
    """Run to GRAB_T and return (frame, tracker_xy, truth_xy, err_series)."""
    src = SceneFrameSource(sc)
    det, trk, ctl = Detector(), Tracker(), Controller()
    pan = tilt = 0.0
    errs = []
    img = est = gt = None
    for i in range(int(GRAB_T * FPS_NOMINAL)):
        t = i * DT
        img = src.frame(t, pan, tilt)
        pred = trk.pos if trk.locked else None
        d = det.detect(img, predict=pred)
        z = (d[0], d[1]) if d else None
        trk.step(z, d[2] if d else 0.0)
        gt = src.truth(t)
        if trk.locked:
            est = trk.pos
            if gt is not None:
                errs.append(math.hypot(est[0] - gt[0], est[1] - gt[1]))
            ex, ey = est[0] - W / 2.0, est[1] - H / 2.0
            dpan, dtilt = ctl.update(ex, ey)
            np_, nt_ = (max(-GIMBAL_LIMIT_DEG, min(GIMBAL_LIMIT_DEG, pan + dpan)),
                        max(-GIMBAL_LIMIT_DEG, min(GIMBAL_LIMIT_DEG, tilt + dtilt)))
            dpan, dtilt = np_ - pan, nt_ - tilt
            pan, tilt = np_, nt_
            trk.ego_shift(dpan, dtilt)
    return img, est, gt, errs


def panel(img, est, gt, errs, label):
    rgb = Image.fromarray(np.dstack([img] * 3), "RGB")
    d = ImageDraw.Draw(rgb)
    if est is not None:
        x, y = est
        r = 26
        d.ellipse([x - r, y - r, x + r, y + r], outline=(0, 230, 200), width=2)
        d.line([x - r - 10, y, x - r + 6, y], fill=(0, 230, 200), width=2)
        d.line([x + r - 6, y, x + r + 10, y], fill=(0, 230, 200), width=2)
        d.line([x, y - r - 10, x, y - r + 6], fill=(0, 230, 200), width=2)
        d.line([x, y + r - 6, x, y + r + 10], fill=(0, 230, 200), width=2)
    if gt is not None:
        d.ellipse([gt[0] - 3, gt[1] - 3, gt[0] + 3, gt[1] + 3], outline=(255, 190, 60), width=2)

    e = float(np.mean(errs)) if errs else float("nan")
    d.rectangle([0, 0, W, 30], fill=(12, 18, 24))
    d.text((8, 9), f"{label}", fill=(235, 240, 245))
    d.text((W - 250, 9), f"mean err {e:6.2f} px = {e*URAD_PER_PX/1000:5.2f} mrad",
           fill=(0, 230, 200))
    d.rectangle([0, 0, W - 1, H - 1], outline=(45, 60, 72), width=1)
    return rgb


def main():
    tiles = []
    for label, sc in PANELS:
        img, est, gt, errs = grab(sc)
        tiles.append(panel(img, est, gt, errs, label))

    sheet = Image.new("RGB", (W * 2 + 24, H * 2 + 24), (12, 18, 24))
    for i, t in enumerate(tiles):
        sheet.paste(t, ((i % 2) * (W + 8) + 8, (i // 2) * (H + 8) + 8))
    sheet.save("evidence_panels.png")
    print("wrote evidence_panels.png", sheet.size)

    # ---- the annexure's required performance log, emitted automatically ----
    from fsoc_spike import main as _  # noqa  (keeps import surface obvious)
    scenarios = [sc for _, sc in PANELS]
    rows = []
    for sc in scenarios:
        r = run(sc)
        p, q = verdict(r)
        r["targets_met"] = f"{p}/{q}"
        rows.append(r)

    log = {
        "problem_statement": "SIH26169",
        "geometry": {
            "sensor_px": [W, H],
            "fov_deg": [4.0, 3.0],
            "deg_per_px": DEG_PER_PX,
            "urad_per_px": round(URAD_PER_PX, 2),
            "slew_cap_deg_s": MAX_SLEW_DEG_S,
        },
        "targets": TARGETS,
        "target_in_angle": {
            "tracking_error_10px_mrad": round(10 * URAD_PER_PX / 1000, 3)
        },
        "runs": rows,
    }
    with open("performance_log.json", "w") as f:
        json.dump(log, f, indent=2)
    print("wrote performance_log.json")


if __name__ == "__main__":
    main()
