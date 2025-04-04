from galaxylocation import GalaxyLocation
from image import Image
from math import dist
import numpy


class GalaxyMasker:
    def __init__(self, image: Image, location: GalaxyLocation) -> None:
        self.image: Image = image
        self.location: GalaxyLocation = location

    def get_galaxy(self) -> Image:
        center = self.location.center
        radius = self.location.radius
        center_x, center_y = center
        return Image(
            self.image[
                center_y - radius : center_y + radius,
                center_x - radius : center_x + radius,
            ]
        )

    def mask_out_galaxy(self) -> Image:
        galaxy_rectangle = self.get_galaxy()

        center = (galaxy_rectangle.shape[0] // 2, galaxy_rectangle.shape[1] // 2)
        radius = self.location.radius

        new_image = numpy.zeros(galaxy_rectangle.data.shape)

        for y in range(galaxy_rectangle.shape[0]):
            for x in range(galaxy_rectangle.shape[1]):
                if dist((x, y), center) > radius:
                    new_image[x, y] = numpy.nan
                else:
                    new_image[y, x] = galaxy_rectangle[x, y]

        return Image(new_image)
