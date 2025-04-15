from galaxyimage import GalaxyImage
from image import Image
import numpy as np


class TemperatureCalculator:
    def __init__(self, r_band_image: GalaxyImage, g_band_image: GalaxyImage, z_band_image: GalaxyImage) -> None:
        self.r_band_image = r_band_image
        self.g_band_image = g_band_image
        self.z_band_image = z_band_image

    def color_index(self, r_minus_z_value: float, g_minus_z_value: float) -> float:
        return r_minus_z_value - g_minus_z_value

    def color_to_kelvin(self, color_index: float) -> float:
        return 4600 * (1 / (0.92 * color_index + 1.7) + 1 / (0.92 * color_index + 0.62))

    def compute_temperature_image(self) -> GalaxyImage:
        r_minus_z_image = self.r_band_image - self.z_band_image
        g_minus_z_image = self.g_band_image - self.z_band_image

        temperature_array = np.zeros(self.r_band_image.shape)

        for y in range(self.r_band_image.shape[0]):
            for x in range(self.r_band_image.shape[1]):
                index = self.color_index(r_minus_z_image[x, y], g_minus_z_image[x, y])
                temperature_array[x, y] = self.color_to_kelvin(index)

        return GalaxyImage(Image(temperature_array))