from GalaxyLoader import GalaxyLoader


class DataLoader:
    def __init__(self, dataset_path: str = "dataset/"):
        self.load_path = dataset_path

    def load_all_galaxies(self) -> GalaxyLoader:
        for galaxy in range(10):
            yield GalaxyLoader(str(galaxy), self.load_path)
