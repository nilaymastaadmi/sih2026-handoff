"""How many subharmonic levels does a Kolmogorov phase screen actually need?

The FFT method under-samples spatial frequencies below 1/(N*delta), where
Kolmogorov turbulence keeps most of its power. Subharmonic augmentation adds it
back. Too few levels and the structure function falls short at large separation,
which shows up as a fitted exponent below 5/3.

This sweeps the level count and reports the fit, so the choice is measured.
"""

import numpy as np

from turbulence import (phase_screen, structure_function_radial, theoretical_D)


def score(levels, N=256, delta=0.005, r0=0.05, n_screens=30, seed=11):
    rng = np.random.default_rng(seed)
    screens = [phase_screen(N, delta, r0, rng, subharmonics=levels)
               for _ in range(n_screens)]
    r, D = structure_function_radial(screens, delta, max_lag=N // 8)
    Dt = theoretical_D(r, r0)
    band = (r / r0 > 0.3) & (r / r0 < 4.0)
    ratio = (D / Dt)[band]
    p = np.polyfit(np.log(r[band]), np.log(D[band]), 1)
    return ratio.mean(), ratio.std(), p[0]


def main():
    print("subharmonic level sweep, Kolmogorov, r0 = 5 cm, 30 screens each")
    print("target: mean ratio 1.000, exponent 1.667")
    print()
    print(f"{'levels':>7} {'mean ratio':>11} {'std':>7} {'exponent':>9}")
    best = None
    for lv in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
        m, s, e = score(lv)
        flag = ""
        if best is None or abs(m - 1.0) < abs(best[1] - 1.0):
            best = (lv, m, e)
        print(f"{lv:7d} {m:11.3f} {s:7.3f} {e:9.3f}{flag}")
    print()
    print(f"closest to unity: {best[0]} levels, ratio {best[1]:.3f}, "
          f"exponent {best[2]:.3f}")


if __name__ == "__main__":
    main()
