from galaxyimage import GalaxyImage
from image import Image
import numpy


class TemperatureCalculator:
    def __init__(self, U: GalaxyImage, B: GalaxyImage, V: GalaxyImage) -> None:
        self.U_image: GalaxyImage = U
        self.B_image: GalaxyImage = B
        self.V_image: GalaxyImage = V

    def calculate_temperature(self, U_V: float, B_V: float) -> float:
        return U_V - B_V

    def compute_temperature_image(self) -> GalaxyImage:
        new_image = numpy.zeros(self.U_image.shape)
        for y in range(self.U_image.shape[0]):
            for x in range(self.U_image.shape[1]):
                new_image[x, y] = self.calculate_temperature(
                    self.U_V_image[x, y],
                    self.B_V_image[x, y],
                )
        return GalaxyImage(Image(new_image))

    @property
    def U_V_image(self) -> GalaxyImage:
        return self.U_image - self.V_image

    @property
    def B_V_image(self) -> GalaxyImage:
        return self.B_image - self.V_image
