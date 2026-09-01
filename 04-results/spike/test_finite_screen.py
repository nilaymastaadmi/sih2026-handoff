"""Is the residual structure-function deficit a bug, or the finite screen?

Kolmogorov theory, D(r) = 6.88 (r/r0)^(5/3), assumes an infinite outer scale. A
simulated screen of finite extent L cannot carry power at scales beyond L, so it
must fall short, and the shortfall must shrink as L/r0 grows.

If the ratio rises toward 1 as the screen grows with everything else fixed, the
deficit is physics and is reportable as such. If it does not, there is a bug.
"""

import numpy as np

from turbulence import phase_screen, structure_function_radial, theoretical_D

DELTA = 0.005
R0 = 0.05
LEVELS = 5


def measure(N, n_screens, seed=23):
    rng = np.random.default_rng(seed)
    screens = [phase_screen(N, DELTA, R0, rng, subharmonics=LEVELS)
               for _ in range(n_screens)]
    # always evaluate over the SAME physical separations, so the comparison is fair
    max_lag = int(0.20 / DELTA)          # up to 0.20 m, i.e. r/r0 up to 4
    r, D = structure_function_radial(screens, DELTA, max_lag=max_lag)
    Dt = theoretical_D(r, R0)
    band = (r / R0 > 0.3) & (r / R0 < 4.0)
    ratio = (D / Dt)[band]
    p = np.polyfit(np.log(r[band]), np.log(D[band]), 1)
    return ratio.mean(), p[0]


def main():
    print("finite-screen test: same delta, same r0, same evaluation band")
    print(f"delta {DELTA*1000:.0f} mm, r0 {R0*100:.0f} cm, {LEVELS} subharmonic levels")
    print("evaluation band fixed at 0.3 < r/r0 < 4 for every grid size")
    print()
    print(f"{'N':>5} {'screen (m)':>11} {'L/r0':>7} {'n':>4} "
          f"{'mean ratio':>11} {'exponent':>9}")
    for N, n in [(128, 60), (256, 40), (512, 16), (1024, 6)]:
        m, e = measure(N, n)
        print(f"{N:5d} {N*DELTA:11.2f} {N*DELTA/R0:7.1f} {n:4d} "
              f"{m:11.3f} {e:9.3f}")
    print()
    print("A ratio rising toward 1.0 with screen size confirms the deficit is the")
    print("finite outer scale of the simulation, not an error in the generator.")


if __name__ == "__main__":
    main()
