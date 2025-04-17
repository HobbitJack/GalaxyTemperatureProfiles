from galaxyloader import GalaxyLoader

from typing import Generator
import h5py
import numpy
import random


class DataLoader:
    def __init__(self, dataset_path: str = "dataset/Dataset.h5"):
        self.load_path = dataset_path

    def load_all_galaxies(self) -> Generator:
        dataset: h5py.File = h5py.File(self.load_path, 'r')
        classification: numpy.ndarray[int] = dataset["ans"]
        filtered_galaxies = [index for index, galaxy_class in enumerate(classification) if int(galaxy_class) in (6, 7)]
        for galaxy_number in random.choices(filtered_galaxies, k=20):
            yield galaxy_number, GalaxyLoader(galaxy_number, self.load_path)
