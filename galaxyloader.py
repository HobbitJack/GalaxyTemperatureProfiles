from image import Image
import numpy

from typing import Generator


class GalaxyLoader:
    def __init__(self, galaxy_name: str, dataset_path: str):
        self.load_path = dataset_path + galaxy_name

    def load_image(self, image_name: str) -> Image:
        return Image(numpy.random.random_sample((1024, 1024)))

    def load_all_images(self) -> Generator:
        # Note: load_all_images is GUARANTEED to yeild in this order
        for image_name in ["Wide.fits", "V.fits", "U.fits", "B.fits"]:
            filt = image_name.strip().split(".")[0]
            yield (filt, self.load_image(str(image_name)))
