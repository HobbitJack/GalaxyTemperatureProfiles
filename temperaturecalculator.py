from galaxyimage import GalaxyImage
from image import Image
import numpy


class TemperatureCalculator:
    """
    Computes pixel-wise blackbody temperature estimates (in Kelvin) from DECaLS R, G, and Z-band images
    using a generalized dual-logarithmic estimator adapted from the blackbody intensity ratio method.

    This estimator is more accurate across temperature ranges, especially at high temperatures,
    by blending two estimates (τ and τ′) using a fitted gamma exponent based on the filter wavelengths.
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

        # Central wavelengths for DECaLS filters in meters (converted from nm)
        self.lambda_g = 477e-9
        self.lambda_r = 623e-9

        # Compute x = hc / (λ k_B) for both bands
        h = 6.626e-34  # Planck constant
        c = 3e8  # speed of light
        kB = 1.381e-23  # Boltzmann constant
        self.x_g = h * c / (self.lambda_g * kB)
        self.x_r = h * c / (self.lambda_r * kB)

        self.n = 4  # photon count proportional regime
        log_ratio = numpy.log(self.x_g / self.x_r)
        self.gamma = 5 - 9 * (abs(log_ratio) + 3) ** -0.252

    def _estimate_temperature(self, intensity_r: float, intensity_g: float) -> float:
        if intensity_r <= 0 or intensity_g <= 0:
            return numpy.nan

        try:
            tau = (self.x_g - self.x_r) / numpy.log(
                intensity_r / intensity_g * (self.x_g / self.x_r) ** (self.n - 1)
            )
            tau_prime = (self.x_g - self.x_r) / numpy.log(
                intensity_r
                / intensity_g
                * (self.x_g / self.x_r) ** (self.n - self.gamma)
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
