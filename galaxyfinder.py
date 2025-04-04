from image import Image
from galaxylocation import GalaxyLocation
import numpy


class GalaxyFinder:
    def __init__(self, image: Image) -> None:
        self.image: Image = image

    def find_galaxy(self) -> GalaxyLocation:
        center = (self.image.shape[0] // 2, self.image.shape[1] // 2)
        return GalaxyLocation(center, numpy.sqrt(numpy.sum(center) // 5))
