from image import Image
from galaxylocation import GalaxyLocation
import numpy


class GalaxyFinder:
    def __init__(self, image: Image) -> None:
        self.image = image

    def find_galaxy(self) -> GalaxyLocation:
        return GalaxyLocation(
            self.image.shape // 2, numpy.sqrt(numpy.sum(self.image.shape // 2)) // 5
        )
