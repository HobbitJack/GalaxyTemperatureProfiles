from image import Image
import numpy
import h5py

from typing import Generator


class GalaxyLoader:
    def __init__(self, galaxy_number: int, dataset_path: str):
        self.load_path = dataset_path
        self.galaxy_number = galaxy_number

    def load_image(self, filt: str) -> Image:
        dataset: h5py.File = h5py.File(self.load_path, "r")
        if filt != "Wide":
            image = dataset["images"][
                self.galaxy_number, :, :, {"G": 0, "R": 1, "Z": 2}[filt]
            ]
            return Image(image)
        else:
            image = sum(
                numpy.array(
                    dataset["images"][self.galaxy_number, :, :, i], dtype="int32"
                )
                for i in range(3)
            )
            return Image(image)

    def load_all_images(self) -> Generator:
        # Note: load_all_images is GUARANTEED to yeild in this order
        for filt in ["Wide", "G", "R", "Z"]:
            yield (filt, self.load_image(filt))
