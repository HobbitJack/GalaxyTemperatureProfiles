#!/usr/bin/python

from image import Image
from galaxylocation import GalaxyLocation
import numpy
import photutils.background
import photutils.segmentation


class GalaxyFinder:
    def __init__(self, image: Image) -> None:
        self.image: Image = image

    def find_galaxy(self) -> GalaxyLocation:
        image_center = (self.image.shape[0] // 2, self.image.shape[1] // 2)

        segment_map = photutils.segmentation.detect_sources(
            self.image.data, numpy.percentile(self.image.data, 75), npixels=30
        )

        deblend = photutils.segmentation.deblend_sources(
            self.image.data, segment_map, npixels=30, nlevels=32, contrast=0.01
        )

        catalogue = photutils.segmentation.SourceCatalog(self.image.data, deblend)

        for index, coord in enumerate(
            zip(
                catalogue.bbox_xmin,
                catalogue.bbox_ymin,
                catalogue.bbox_xmax,
                catalogue.bbox_ymax,
            )
        ):
            x, y, X, Y = coord
            if (x < image_center[0] < X) and (y < image_center[0] < Y):
                center = catalogue.centroid_win[index]
                radius = int(catalogue.equivalent_radius[index].value)

        return GalaxyLocation(center, radius)


def main():
    import h5py
    import random
    import matplotlib.pyplot

    dataset = h5py.File("dataset/Dataset.h5")
    data_images = [
        index for index, key in enumerate(dataset["ans"]) if (key == 6 or key == 7)
    ]

    image: Image = Image(dataset["images"][random.choice(data_images), :, :, 2])

    galaxy_finder = GalaxyFinder(image)
    galaxy_location = galaxy_finder.find_galaxy()

    matplotlib.pyplot.imshow(image.data)
    matplotlib.pyplot.scatter(
        [galaxy_location.center[0]], [galaxy_location.center[1]], marker="+"
    )
    matplotlib.pyplot.colorbar()

    matplotlib.pyplot.gca().add_artist(
        matplotlib.pyplot.Circle(
            galaxy_location.center,
            galaxy_location.radius,
            fill=False,
            color="Red",
        )
    )

    matplotlib.pyplot.savefig("output/finder.png")


if __name__ == "__main__":
    main()
