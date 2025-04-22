from galaxyloader import GalaxyLoader

from typing import Generator
import h5py
import numpy
import random


class DataLoader:
    """
    Loads all of the images in the data set

    Attributes:
        load_path (str): Path to where the data is stored
    """
    def __init__(self, dataset_path: str = "dataset/Dataset.h5"):
        """
        Initializes a DataLoader object

        Parameters:
            dataset_path (str): passes to load_path attribute
        """
        self.load_path = dataset_path

    def load_all_galaxies(self) -> Generator:
        """
        Loads all of the galaxies in the data set

        Returns:
            galaxy_number (int): Number of each galaxy loaded in
            GalaxyLoader (GalaxyLoader): GalaxyLoader object for the galaxy number
        """
        dataset: h5py.File = h5py.File(self.load_path, "r")
        classification: numpy.ndarray[int] = dataset["ans"]
        # creates a list of galaxies filtered to only types 6 and 7 which unbarred tight spirals
        # and unbarred loose spirals respectively 
        filtered_galaxies = [
            index
            for index, galaxy_class in enumerate(classification)
            if int(galaxy_class) in (6, 7)
        ]
        # passes a random selection of the filtered galaxies into a GalaxyLoader class
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
