from galaxyimage import GalaxyImage
from image import Image
import numpy


# Central wavelengths for DECaLS filters in meters (converted from nm)
LAMBDA_G = 477e-9
LAMBDA_R = 623e-9

# Compute x = hc / (λ k_B) for both bands
h = 6.626e-34  # Planck constant
c = 3e8  # speed of light
kB = 1.381e-23  # Boltzmann constant
X_G = h * c / (LAMBDA_G * kB)
X_R = h * c / (LAMBDA_R * kB)

GAMMA = 5 - 9 * (numpy.log(X_G / X_R) + 3) ** -0.252


class TemperatureCalculator:
    """
        Computes pixel-wise blackbody temperature estimates (in Kelvin) from DECaLS R, G, and Z-band images
        using a generalized dual-logarithmic estimator adapted from the blackbody intensity ratio method.

        This estimator is more accurate across temperature ranges, especially at high temperatures,
        by blending two estimates (τ and τ′) using a fitted gamma exponent based on the filter wavelengths.

    Uses https://iopscience.iop.org/article/10.1209/0295-5075/97/34008, specifically Eqs (9), (11), (13).
    """

    def __init__(
        self,
        r_band_image: GalaxyImage,
        g_band_image: GalaxyImage,
        z_band_image: GalaxyImage,
    ) -> None:
        self.r_band_image = r_band_image
        self.g_band_image = g_band_image
        self.z_band_image = z_band_image

    def _estimate_temperature(self, intensity_r: float, intensity_g: float) -> float:
        if intensity_r <= 0 or intensity_g <= 0:
            return numpy.nan

        try:
            tau = (X_G - X_R) / numpy.log(
                intensity_r / intensity_g * (X_G / X_R) ** 3  # N = 4; N-1 -> 3
            )
            tau_prime = (X_G - X_R) / numpy.log(
                intensity_r / intensity_g * (X_G / X_R) ** (4 - GAMMA)
            )
            T = (tau + tau_prime) / 2
            return T if T > 0 else numpy.nan
        except (ZeroDivisionError, FloatingPointError):
            return numpy.nan

    def compute_temperature_image(self) -> GalaxyImage:
        height, width = self.r_band_image.shape
        temp_array = numpy.zeros((height, width))

        for y in range(height):
            for x in range(width):
                r = self.r_band_image[y, x]
                g = self.g_band_image[y, x]
                temp_array[y, x] = self._estimate_temperature(r, g)

        return GalaxyImage(Image(temp_array))
