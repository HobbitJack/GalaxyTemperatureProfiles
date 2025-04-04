from galaxyloader import GalaxyLoader

from typing import Generator


class DataLoader:
    def __init__(self, dataset_path: str = "dataset/"):
        self.load_path = dataset_path

    def load_all_galaxies(self) -> Generator:
        for galaxy_name in range(10):
            yield galaxy_name, GalaxyLoader(str(galaxy_name), self.load_path)
