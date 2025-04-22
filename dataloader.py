from galaxyloader import GalaxyLoader

from typing import Generator
import h5py
import numpy
import random


class DataLoader:
    def __init__(self, dataset_path: str = "dataset/Dataset.h5"):
        self.load_path = dataset_path

    def load_all_galaxies(self) -> Generator:
        dataset: h5py.File = h5py.File(self.load_path, "r")
        classification: numpy.ndarray[int] = dataset["ans"]
        filtered_galaxies = [
            index
            for index, galaxy_class in enumerate(classification)
            if int(galaxy_class) in (6, 7)
        ]
        for galaxy_number in random.choices(filtered_galaxies, k=10):
            yield galaxy_number, GalaxyLoader(galaxy_number, self.load_path)


if __name__ == "__main__":
    import matplotlib.pyplot

    dataloader = DataLoader()
    for galaxyloader in dataloader.load_all_galaxies():
        images = [image for band, image in galaxyloader[1].load_all_images()]
        wide, g, r, z = images
        matplotlib.pyplot.imshow(
            numpy.array(r.data, dtype="int16") - numpy.array(g.data, dtype="int16")
        )
        matplotlib.pyplot.colorbar()
        matplotlib.pyplot.show()
