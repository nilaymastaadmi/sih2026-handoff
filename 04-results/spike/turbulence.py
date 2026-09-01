"""Physically defensible atmospheric turbulence for PS 26169.

Replaces the placeholder "reduce contrast and brightness" model with Kolmogorov
and von Karman phase screens, and then VALIDATES them against theory rather than
asserting they are correct.

The validation is the point. A generated screen is only a turbulence model if its
phase structure function matches

    D_phi(r) = 6.88 * (r / r0) ** (5/3)

for Kolmogorov statistics. Anything that merely looks grainy is not turbulence,
and an optics evaluator can tell the difference in seconds.

numpy only.
"""

import numpy as np

# ---------------------------------------------------------------------------
# Atmospheric parameters
# ---------------------------------------------------------------------------
def r0_from_cn2(cn2, wavelength_m, path_len_m):
    """Fried parameter for a plane wave over a uniform path.

        r0 = (0.423 * k^2 * Cn2 * L) ** (-3/5)
    """
    k = 2 * np.pi / wavelength_m
    return (0.423 * k * k * cn2 * path_len_m) ** (-3.0 / 5.0)


def rytov_variance(cn2, wavelength_m, path_len_m):
    """Plane-wave Rytov variance; >1 indicates strong scintillation."""
    k = 2 * np.pi / wavelength_m
    return 1.23 * cn2 * k ** (7.0 / 6.0) * path_len_m ** (11.0 / 6.0)


# ---------------------------------------------------------------------------
# Phase screens
# ---------------------------------------------------------------------------
def _psd(f, r0, L0=None, l0=None, kolmogorov=True):
    """Phase PSD. Kolmogorov, or von Karman with outer/inner scales."""
    with np.errstate(divide="ignore", invalid="ignore"):
        if kolmogorov:
            psd = 0.023 * r0 ** (-5.0 / 3.0) * f ** (-11.0 / 3.0)
        else:
            f0 = 1.0 / L0
            fm = 5.92 / l0 / (2 * np.pi)
            psd = (0.023 * r0 ** (-5.0 / 3.0)
                   * np.exp(-((f / fm) ** 2))
                   / (f * f + f0 * f0) ** (11.0 / 6.0))
    psd[~np.isfinite(psd)] = 0.0
    return psd


def phase_screen(N, delta, r0, rng, L0=100.0, l0=0.01,
                 kolmogorov=True, subharmonics=5):
    """One phase screen, radians, on an N x N grid of spacing `delta` metres.

    The FFT method alone under-represents power at spatial frequencies below
    1/(N*delta). Kolmogorov turbulence has most of its power there, so without
    subharmonic augmentation the structure function falls short at large r.
    That correction is why this validates and a naive implementation does not.
    """
    df = 1.0 / (N * delta)
    fx = (np.arange(-N // 2, N // 2)) * df
    FX, FY = np.meshgrid(fx, fx)
    f = np.sqrt(FX * FX + FY * FY)

    psd = _psd(f, r0, L0, l0, kolmogorov)
    psd[N // 2, N // 2] = 0.0            # remove the (undefined) piston term

    cn = ((rng.normal(size=(N, N)) + 1j * rng.normal(size=(N, N)))
          * np.sqrt(psd) * df)
    scr = np.real(np.fft.ifft2(np.fft.ifftshift(cn)) * N * N)

    # low-frequency (subharmonic) augmentation
    x = (np.arange(-N // 2, N // 2)) * delta
    X, Y = np.meshgrid(x, x)
    lo = np.zeros((N, N))
    for p in range(1, subharmonics + 1):
        dfp = df / (3.0 ** p)
        fxp = np.array([-1.0, 0.0, 1.0]) * dfp
        FXp, FYp = np.meshgrid(fxp, fxp)
        fp = np.sqrt(FXp * FXp + FYp * FYp)
        psdp = _psd(fp, r0, L0, l0, kolmogorov)
        psdp[1, 1] = 0.0
        cnp = ((rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3)))
               * np.sqrt(psdp) * dfp)
        for i in range(3):
            for j in range(3):
                lo += np.real(cnp[i, j] * np.exp(2j * np.pi
                                                 * (FXp[i, j] * X + FYp[i, j] * Y)))
    scr = scr + lo
    return scr - scr.mean()


# ---------------------------------------------------------------------------
# Validation: measured structure function against theory
# ---------------------------------------------------------------------------
def structure_function_radial(screens, delta, max_lag):
    """D(r) = < |phi(x+r) - phi(x)|^2 >, averaged over screens and both axes."""
    lags = np.arange(1, max_lag + 1)
    D = np.zeros(len(lags))
    for k, lag in enumerate(lags):
        acc, n = 0.0, 0
        for s in screens:
            dx = s[:, lag:] - s[:, :-lag]
            dy = s[lag:, :] - s[:-lag, :]
            acc += float((dx * dx).sum() + (dy * dy).sum())
            n += dx.size + dy.size
        D[k] = acc / n
    return lags * delta, D


def theoretical_D(r, r0):
    return 6.88 * (r / r0) ** (5.0 / 3.0)


def validate(N=256, delta=0.005, r0=0.05, n_screens=40, seed=1):
    """Generate screens and compare D(r) to 6.88 (r/r0)^(5/3)."""
    rng = np.random.default_rng(seed)
    screens = [phase_screen(N, delta, r0, rng) for _ in range(n_screens)]
    r, D = structure_function_radial(screens, delta, max_lag=N // 8)
    Dt = theoretical_D(r, r0)
    ratio = D / Dt
    return r, D, Dt, ratio, screens


# ---------------------------------------------------------------------------
# Imaging a beacon through the screen
# ---------------------------------------------------------------------------
def psf_from_screen(screen, delta, wavelength_m, aperture_m, out=64):
    """Short-exposure PSF for a circular aperture behind a phase screen."""
    N = screen.shape[0]
    x = (np.arange(-N // 2, N // 2)) * delta
    X, Y = np.meshgrid(x, x)
    pupil = (np.sqrt(X * X + Y * Y) <= aperture_m / 2.0).astype(float)
    if pupil.sum() == 0:
        pupil[N // 2, N // 2] = 1.0
    field = pupil * np.exp(1j * screen)
    img = np.abs(np.fft.fftshift(np.fft.fft2(np.fft.ifftshift(field)))) ** 2
    c = N // 2
    h = out // 2
    cut = img[c - h:c + h, c - h:c + h]
    m = cut.max()
    return cut / m if m > 0 else cut


def spot_metrics(psf):
    """Centroid offset from the frame centre, and a normalised second moment."""
    n = psf.shape[0]
    yy, xx = np.mgrid[0:n, 0:n]
    tot = psf.sum()
    if tot <= 0:
        return 0.0, 0.0
    cx = float((psf * xx).sum() / tot)
    cy = float((psf * yy).sum() / tot)
    c = (n - 1) / 2.0
    wander = float(np.hypot(cx - c, cy - c))
    var = float((psf * ((xx - cx) ** 2 + (yy - cy) ** 2)).sum() / tot)
    return wander, float(np.sqrt(var))


def main():
    print("Turbulence model validation for PS 26169")
    print("=" * 78)

    N, delta, r0 = 256, 0.005, 0.05
    print(f"grid {N}x{N}, sample {delta*1000:.1f} mm, r0 = {r0*100:.1f} cm, "
          f"screen {N*delta:.2f} m across")
    r, D, Dt, ratio, screens = validate(N=N, delta=delta, r0=r0)

    print()
    print("phase structure function, measured vs theory D(r) = 6.88 (r/r0)^(5/3)")
    print(f"{'r (m)':>8} {'r/r0':>7} {'measured':>11} {'theory':>11} {'ratio':>7}")
    for i in range(0, len(r), max(1, len(r) // 10)):
        print(f"{r[i]:8.3f} {r[i]/r0:7.2f} {D[i]:11.3f} {Dt[i]:11.3f} {ratio[i]:7.3f}")

    band = (r / r0 > 0.3) & (r / r0 < 4.0)
    print()
    print(f"mean ratio over 0.3 < r/r0 < 4 : {ratio[band].mean():.3f} "
          f"(1.000 is exact)")
    print(f"spread (std) over that band    : {ratio[band].std():.3f}")

    # fitted power-law exponent, should be 5/3 = 1.667
    p = np.polyfit(np.log(r[band]), np.log(D[band]), 1)
    print(f"fitted exponent                 : {p[0]:.3f}  (theory 1.667)")

    print()
    print("=" * 78)
    print("beacon spot through turbulence, 1550 nm, 10 km path, 5 cm aperture")
    wl, L, ap = 1550e-9, 10_000.0, 0.05
    print(f"{'Cn2':>10} {'r0 (cm)':>9} {'D/r0':>7} {'Rytov':>8} "
          f"{'wander px':>10} {'spot rms':>9}")
    rng = np.random.default_rng(7)
    for cn2 in [1e-16, 1e-15, 5e-15, 1e-14, 5e-14, 1e-13]:
        r0c = r0_from_cn2(cn2, wl, L)
        ry = rytov_variance(cn2, wl, L)
        ws, ss = [], []
        for _ in range(12):
            scr = phase_screen(128, ap / 64.0, max(r0c, 1e-4), rng)
            psf = psf_from_screen(scr, ap / 64.0, wl, ap, out=48)
            w, s = spot_metrics(psf)
            ws.append(w)
            ss.append(s)
        print(f"{cn2:10.0e} {r0c*100:9.2f} {ap/max(r0c,1e-9):7.2f} {ry:8.3f} "
              f"{np.mean(ws):10.2f} {np.mean(ss):9.2f}")

    print()
    print("Interpretation: as Cn2 rises, r0 falls, D/r0 grows, the spot breaks up")
    print("and its centroid wanders. That wander is the physical quantity a coarse")
    print("tracker must follow, and the reason a contrast-reduction model is not")
    print("an acceptable stand-in.")


if __name__ == "__main__":
    main()
