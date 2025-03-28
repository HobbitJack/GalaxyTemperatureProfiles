from galaxylocation import GalaxyLocation
from image import Image
from math import dist
import numpy


class GalaxyMasker:
    def __init__(self, image: Image, location: GalaxyLocation) -> None:
        self.image: Image = image
        self.location: GalaxyLocation = location

    def get_galaxy(self) -> Image:
        center, radius = self.location
        center_x, center_y = center
        return self.image[
            center_x - radius : center_x + radius, center_y - radius : center_y + radius
        ]

    def mask_out_galaxy(self) -> Image:
        galaxy_rectangle = self.get_galaxy()

        center = galaxy_rectangle.shape // 2
        radius = self.location.radius

        new_image = numpy.zeros(galaxy_rectangle.data.shape)

        for x in range(galaxy_rectangle.shape[0]):
            for y in range(galaxy_rectangle.shape[1]):
                array_x, array_y = galaxy_rectangle.get_array_index(x, y)
                if dist((x, y), center) > radius:
                    new_image[array_x, array_y] = numpy.nan
                else:
                    new_image[array_y, array_x] = galaxy_rectangle[x, y]

        return Image(new_image)
