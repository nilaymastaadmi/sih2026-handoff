"""Learned spot scorer for PS 26169: the AI component, measured.

The spike's measured failure mode is detection under impulse noise: a salt
pixel can win the argmax and capture the lock (worst frame 451 px under 10%
salt-and-pepper). This module trains a small logistic scorer on 21x21 patches
(beacon point-spread function vs impulse/noise), ranks the top-K candidate
peaks with it, and re-runs the spike's 11 scenarios classical vs AI-assisted
under identical conditions.

Labels are free: the simulator knows where the beacon is. No external data,
no GPU; numpy only. Honest by construction: whatever the A/B shows is what
ships on the slide, including a negative result.

Run: python ai_scorer.py   (writes ai_scorer_results.json)
"""

import json
import math

import numpy as np

import fsoc_spike as fs

P = 21          # patch size
HALF = P // 2
TOPK = 6
SCORE_FLOOR = 0.5
RNG = np.random.default_rng(2026)


# ---------------------------------------------------------------- training data
def synth_patch(positive):
    gain = float(RNG.uniform(0.35, 1.0))
    off = float(RNG.uniform(-5, 25))
    bg = 18.0 * gain + off
    img = np.full((P, P), bg, np.float32)
    if positive:
        spot = float(RNG.uniform(5, 20))
        sigma = max(0.7, spot / 4.0) + float(RNG.uniform(0.8, 2.2))
        cx = HALF + float(RNG.uniform(-2, 2))
        cy = HALF + float(RNG.uniform(-2, 2))
        yy, xx = np.mgrid[0:P, 0:P].astype(np.float32)
        img += 210.0 * gain * np.exp(-((xx - cx) ** 2 + (yy - cy) ** 2) / (2 * sigma * sigma))
    img += RNG.normal(0, float(RNG.uniform(4, 20)), img.shape).astype(np.float32)
    n_imp = int(RNG.integers(0, 4)) if positive else int(RNG.integers(1, 7))
    for _ in range(n_imp):
        # impulses biased toward the centre: the confuser is a spike AT the peak
        ix = int(np.clip(RNG.normal(HALF, 4), 0, P - 1))
        iy = int(np.clip(RNG.normal(HALF, 4), 0, P - 1))
        img[iy, ix] = 255.0 if RNG.random() < 0.5 else 0.0
    img = np.clip(img, 0, 255)
    med = float(np.median(img))
    mad = float(np.median(np.abs(img - med))) + 1e-6
    return ((img - med) / (1.4826 * mad)).clip(-10, 60).reshape(-1) / 10.0


def train(n_per_class=8000, epochs=300, lr=0.5, l2=1e-4):
    X = np.stack([synth_patch(i < n_per_class) for i in range(2 * n_per_class)])
    y = np.concatenate([np.ones(n_per_class), np.zeros(n_per_class)])
    idx = RNG.permutation(len(y))
    X, y = X[idx], y[idx]
    w = np.zeros(X.shape[1])
    b = 0.0
    n = len(y)
    for _ in range(epochs):
        z = X @ w + b
        p = 1.0 / (1.0 + np.exp(-z))
        g = p - y
        w -= lr * (X.T @ g / n + l2 * w)
        b -= lr * float(g.mean())
    acc = float((((X @ w + b) > 0) == (y > 0.5)).mean())
    return w, b, acc


def extract_patch(img, cx, cy):
    x0, y0 = int(round(cx)) - HALF, int(round(cy)) - HALF
    x0 = max(0, min(fs.W - P, x0))
    y0 = max(0, min(fs.H - P, y0))
    p = img[y0:y0 + P, x0:x0 + P].astype(np.float32)
    med = float(np.median(p))
    mad = float(np.median(np.abs(p - med))) + 1e-6
    return ((p - med) / (1.4826 * mad)).clip(-10, 60).reshape(-1) / 10.0


class AIDetector(fs.Detector):
    """The spike's detector with a learned candidate re-ranker: top-K peaks on
    the smoothed map, each scored on the raw image patch, best score wins."""

    def __init__(self, w, b, k=6.0, win=9):
        super().__init__(k=k, win=win)
        self.w, self.b = w, b

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
        thr = med + self.k * (sigma / 3.0)

        if predict is not None:
            px, py = predict
            rx0, rx1 = int(max(0, px - roi)), int(min(fs.W, px + roi + 1))
            ry0, ry1 = int(max(0, py - roi)), int(min(fs.H, py + roi + 1))
            if rx1 - rx0 < 3 or ry1 - ry0 < 3:
                return None
            view = sm[ry0:ry1, rx0:rx1].copy()
            ox, oy, kk = rx0, ry0, 3
        else:
            view = sm.copy()
            ox, oy, kk = 0, 0, TOPK

        best = None
        for _ in range(kk):
            jy, jx = np.unravel_index(int(np.argmax(view)), view.shape)
            if view[jy, jx] < thr:
                break
            iy, ix = jy + oy, jx + ox
            score = 1.0 / (1.0 + math.exp(-(float(extract_patch(f, ix, iy) @ self.w) + self.b)))
            if best is None or score > best[0]:
                best = (score, ix, iy)
            y0, y1 = max(0, jy - 8), min(view.shape[0], jy + 9)
            x0, x1 = max(0, jx - 8), min(view.shape[1], jx + 9)
            view[y0:y1, x0:x1] = -1e9
        if best is None or best[0] < SCORE_FLOOR:
            return None
        _, ix, iy = best

        w_ = self.win
        y0, y1 = max(0, iy - w_), min(fs.H, iy + w_ + 1)
        x0, x1 = max(0, ix - w_), min(fs.W, ix + w_ + 1)
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


def scenarios():
    S = fs.Scenario
    return [
        S("baseline clear circular", motion="circular"),
        S("straight line, haze", motion="straight", atmosphere="haze", noise_sigma=10),
        S("figure8, rain", motion="figure8", atmosphere="rain", noise_sigma=12),
        S("random walk, lowlight", motion="random", atmosphere="lowlight", noise_sigma=10),
        S("fog + poisson", motion="circular", atmosphere="fog", noise_sigma=14, poisson=True),
        S("salt&pepper 10% (annexure max)", motion="circular", salt_pepper=0.10, noise_sigma=8),
        S("jitter 20px/frame (max)", motion="circular", jitter_px=20.0, noise_sigma=8),
        S("platform 20px/frame (max)", motion="circular", platform_px=20.0, noise_sigma=8),
        S("small spot 5px", motion="circular", spot_px=5.0, noise_sigma=8),
        S("large spot 20px", motion="circular", spot_px=20.0, noise_sigma=8),
        S("WORST CASE all-max", motion="random", atmosphere="fog", noise_sigma=20,
          salt_pepper=0.10, poisson=True, jitter_px=20.0, platform_px=20.0, spot_px=8.0),
    ]


def main():
    print("training the spot scorer (numpy logistic, 21x21 patches)...")
    w, b, acc = train()
    print(f"  training accuracy: {acc:.4f} on 16,000 synthetic patches")

    orig = fs.Detector
    out = {"train_acc": acc, "classical": {}, "ai": {}}
    for label, det_cls in (("classical", orig),
                           ("ai", lambda k=6.0, win=9: AIDetector(w, b, k=k, win=win))):
        fs.Detector = det_cls
        print(f"\n--- {label} ---")
        passed = 0
        for sc in scenarios():
            r = fs.run(sc)
            p, q = fs.verdict(r)
            passed += (p == q)
            out[label][r["scenario"]] = {k: (round(v, 3) if isinstance(v, float) else v)
                                         for k, v in r.items() if k != "scenario"}
            print(fs.fmt(r))
        out[label]["scenarios_passing_all_targets"] = passed
        print(f"  passing all 5 targets: {passed} of 11")
    fs.Detector = orig

    with open("ai_scorer_results.json", "w") as f:
        json.dump(out, f, indent=1)
    print("\nwrote ai_scorer_results.json")

    for name in ("salt&pepper 10% (annexure max)", "WORST CASE all-max", "random walk, lowlight"):
        c, a = out["classical"][name], out["ai"][name]
        print(f"{name}: mean {c['err_mean_px']} -> {a['err_mean_px']} px, "
              f"max {c['err_max_px']} -> {a['err_max_px']} px, "
              f"loss {c['loss_pct']} -> {a['loss_pct']} %")


if __name__ == "__main__":
    main()
