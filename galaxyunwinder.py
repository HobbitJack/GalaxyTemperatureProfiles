from galaxyimage import GalaxyImage
import numpy


class GalaxyUnwinder:
    def __init__(self, image: GalaxyImage) -> None:
        self.image = image

    def unwind(self) -> numpy.ndarray:
        return numpy.random.random_sample((360, GalaxyImage.radius))
