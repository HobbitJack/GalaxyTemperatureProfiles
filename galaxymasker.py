#!/usr/bin/python

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


if __name__ == "__main__":
    import h5py
    import random
    import matplotlib.pyplot
    from galaxyfinder import GalaxyFinder

    dataset = h5py.File("dataset/Dataset.h5")
    data_images = [
        index for index, key in enumerate(dataset["ans"]) if (key == 6 or key == 7)
    ]

    image: Image = Image(dataset["images"][random.choice(data_images), :, :, 2])

    galaxy_finder = GalaxyFinder(image)
    galaxy_location = galaxy_finder.find_galaxy()

    galaxy_masker = GalaxyMasker(image, galaxy_location)

    mask_image = galaxy_masker.mask_out_galaxy()

    matplotlib.pyplot.imshow(mask_image.data)

    matplotlib.pyplot.gca().add_artist(
        matplotlib.pyplot.Circle(
            (mask_image.shape[0] // 2, mask_image.shape[1] // 2),
            galaxy_location.radius,
            fill=False,
            color="Red",
        )
    )
    matplotlib.pyplot.savefig("output/mask.png")
