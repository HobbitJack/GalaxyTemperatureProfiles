from image import Image
import numpy
import h5py

from typing import Generator


class GalaxyLoader:
    """
    Class for loading in galaxies as images

    Attributes: 
        load_path (str): directs where the data loads from
        galaxy_number (int): number of the galaxy in the header of the h5py file
    """
    def __init__(self, galaxy_number: int, dataset_path: str):
        """
        Initializes a galaxy loader object

        Parameters:
            galaxy_number (int): passed to galaxy_number attribute
            dataset_path (str): passed to load_path attribute
        """
        self.load_path = dataset_path
        self.galaxy_number = galaxy_number

    def load_image(self, filt: str) -> Image:
        """
        Loads an individual image from the data set

        Parameters:
            filt (str): which filter for data, g, r, z, or wide band
        
        Returns:
            image (Image): image of the galaxy passed through the Image class
        """
        dataset: h5py.File = h5py.File(self.load_path, "r")
        # Creates an image that is not wide band
        if filt != "Wide":
            # Indexes the galaxy number, every x value, every y value, and the filter that was chosen
            image = dataset["images"][
                self.galaxy_number, :, :, {"G": 0, "R": 1, "Z": 2}[filt]
            ]
            return Image(image)
        #Creates a wide band image by summing all the other bands
        else:
            image = sum(
                dataset["images"][self.galaxy_number, :, :, i] for i in range(3)
            )
            return Image(image)

    def load_all_images(self) -> Generator:
        """
        Iterates over each filter type and loads each image for those filters
        """
        # Note: load_all_images is GUARANTEED to yeild in this order
        for filt in ["Wide", "G", "R", "Z"]:
            yield (filt, self.load_image(filt))
