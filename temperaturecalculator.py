from galaxyimage import GalaxyImage
from image import Image
import numpy as np

class TemperatureCalculator:
    """
    TemperatureCalculator

    This class computes the effective temperature (in Kelvin) of each pixel in a galaxy image
    using an empirical color–temperature relation based on the difference between R and G band images.

    Methodology:
    1. The color index is defined as (R - G), analogous to (B - V) in classical photometry.
    2. The temperature is computed using a modified Ballesteros formula:
           T = 4600 * [ 1 / (0.92*C + 1.7) + 1 / (0.92*C + 0.62) ]
       where C is the color index.
    3. Temperatures are only computed for pixels with color indices in the range (–1.5, 2.0).
       Pixels outside this range are assigned NaN to avoid unphysical values.

    Attributes:
        r_band_image (GalaxyImage): R-band flux image.
        g_band_image (GalaxyImage): G-band flux image.
        z_band_image (GalaxyImage): Z-band flux image (not used in the current formula).

    Methods:
        compute_temperature_image() -> GalaxyImage:
            Returns a GalaxyImage containing the 2D map of effective temperatures in Kelvin.
    """

    def __init__(self, r_band_image: GalaxyImage, g_band_image: GalaxyImage, z_band_image: GalaxyImage) -> None:
        self.r_band_image = r_band_image
        self.g_band_image = g_band_image
        self.z_band_image = z_band_image

    def color_index(self, r_value: float, g_value: float) -> float:
        return r_value - g_value

    def color_to_kelvin(self, color_index: float) -> float:
        if not -1.5 < color_index < 2.0:
            return np.nan
        temp = 4600 * (1 / (0.92 * color_index + 1.7) + 1 / (0.92 * color_index + 0.62))
        return temp if temp > 0 else np.nan

    def compute_temperature_image(self) -> GalaxyImage:
        height, width = self.r_band_image.shape
        temperature_array = np.zeros((height, width))

        for y in range(height):
            for x in range(width):
                r = self.r_band_image[y, x]
                g = self.g_band_image[y, x]
                index = self.color_index(r, g)
                temperature_array[y, x] = self.color_to_kelvin(index)

        return GalaxyImage(Image(temperature_array))