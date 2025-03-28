#!/usr/bin/python

from dataloader import DataLoader
from galaxyfinder import GalaxyFinder
from galaxyimage import GalaxyImage
from galaxylocation import GalaxyLocation
from galaxymasker import GalaxyMasker
from galaxyunwinder import GalaxyUnwinder
from image import Image
import numpy
from radialaverager import RadialAverager
from temperaturecalculator import TemperatureCalculator
from temperatureprofile import TemperatureProfile


def main() -> None:
    data_loader: DataLoader = DataLoader()
    for galaxy_name, galaxy in data_loader.load_all_galaxies():

        wide_image: Image = next(galaxy.load_all_images())
        galaxy_finder: GalaxyFinder = GalaxyFinder(wide_image)
        galaxy_location: GalaxyLocation = galaxy_finder.find_galaxy()

        filtered_galaxy_images: dict[str, GalaxyImage] = {}

        # U, V, B
        for filt, image in galaxy.load_all_images():
            galaxy_masker: GalaxyMasker = GalaxyMasker(image, galaxy_location)
            filter_image: GalaxyImage = GalaxyImage(galaxy_masker.mask_out_galaxy())
            filtered_galaxy_images[filt] = filter_image

        temperature_calculator: TemperatureCalculator = TemperatureCalculator(
            filtered_galaxy_images["U"],
            filtered_galaxy_images["B"],
            filtered_galaxy_images["V"],
        )
        temperature_image = temperature_calculator.compute_temperature_image()

        galaxy_unwinder: GalaxyUnwinder = GalaxyUnwinder(temperature_image)
        radial_data: numpy.ndarray = galaxy_unwinder.unwind()

        temperature_averager = RadialAverager(radial_data)
        temperature_data = temperature_averager.compute_average()
        temperature_profile = TemperatureProfile(temperature_data)

        temperature_profile.plot_temperature(galaxy_name)


if __name__ == "__main__":
    main()
