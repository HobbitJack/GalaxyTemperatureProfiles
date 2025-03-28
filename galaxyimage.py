from image import Image
import numpy


class GalaxyImage(Image):
    def __init__(self, image: Image) -> None:
        super().__init__(image.data)

    @property
    def center(self):
        return self.shape // 2

    @property
    def radius(self):
        return 2 * numpy.sqrt(self.shape[0] ** 2 + self.shape[1] ** 2)
