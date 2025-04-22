#!/usr/bin/python

import numpy
from dataloader import DataLoader
from galaxyfinder import GalaxyFinder
from galaxylocation import GalaxyLocation
from galaxymasker import GalaxyMasker
from galaxyimage import GalaxyImage
from galaxyunwinder import GalaxyUnwinder
from image import Image
from radialaverager import RadialAverager
from temperaturecalculator import TemperatureCalculator
from temperatureprofile import TemperatureProfile

"""
galaxy_temp.py

This script processes galaxy images stored in HDF5 (.h5) format to generate temperature profiles.

Workflow:
1. Load R-band, G-band, and Z-band images from the .h5 file.
2. Automatically find the location of the galaxy using the R-band.
3. Mask everything outside the galaxy to clean up noise.
4. Calculate a temperature map using color differences between bands.
5. Unwind the image radially.
6. Compute the radial average temperature profile.
7. Plot and save the temperature profile as a .png.

This allows us to visualize how the temperature changes as we move outward from the galaxy center.
"""

data_loader: DataLoader = DataLoader()
for galaxy_number, galaxy in data_loader.load_all_galaxies():
    galaxy_images: dict[str, Image] = {}
    for band, image in galaxy.load_all_images():
        galaxy_images[band] = image

    galaxy_finder: GalaxyFinder = GalaxyFinder(galaxy_images["Z"])
    galaxy_location: GalaxyLocation = galaxy_finder.find_galaxy()

    mask_images: dict[str, Image] = {}
    for band, image in galaxy_images.items():
        galaxy_masker: GalaxyMasker = GalaxyMasker(image, galaxy_location)
        mask_images[band] = galaxy_masker.mask_out_galaxy()

    temperature_calculator: TemperatureCalculator = TemperatureCalculator(
        mask_images["R"], mask_images["G"], mask_images["Z"]
    )

    temperature_image: GalaxyImage = temperature_calculator.compute_temperature_image()

    galaxy_unwinder: GalaxyUnwinder = GalaxyUnwinder(temperature_image)
    temperature_unwound: numpy.ndarray = galaxy_unwinder.unwind()

    radial_averager: RadialAverager = RadialAverager(temperature_unwound)
    temperature_profile: TemperatureProfile = TemperatureProfile(
        radial_averager.compute_average()
    )
    temperature_profile.plot_temperature(galaxy_number)
