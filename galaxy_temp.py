#!/usr/bin/python

import numpy as np
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
import logging


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def process_galaxy(galaxy_name: str, galaxy) -> None:
    logging.info(f"Processing galaxy: {galaxy_name}")

    try:
        galaxy_location = find_galaxy_location(galaxy)
        filtered_images = mask_galaxy_images(galaxy, galaxy_location)

        if not all(f in filtered_images for f in ("U", "B", "V")):
            logging.warning(f"Missing U, B, or V filters for {galaxy_name}. Skipping...")
            return

        temperature_profile = compute_temperature_profile(filtered_images)
        plot_temperature_profile(galaxy_name, temperature_profile)

    except Exception as e:
        logging.error(f"Failed to process {galaxy_name}: {e}")


def find_galaxy_location(galaxy) -> GalaxyLocation:
    wide_image: Image = next(galaxy.load_all_images())
    galaxy_finder = GalaxyFinder(wide_image)
    location = galaxy_finder.find_galaxy()
    logging.info(f"Found galaxy location at {location}")
    return location


def mask_galaxy_images(galaxy, location: GalaxyLocation) -> dict[str, GalaxyImage]:
    images: dict[str, GalaxyImage] = {}
    for filt, image in galaxy.load_all_images():
        masker = GalaxyMasker(image, location)
        masked_image = GalaxyImage(masker.mask_out_galaxy())
        images[filt] = masked_image
        logging.info(f"Masked {filt}-band image")
    return images


def compute_temperature_profile(images: dict[str, GalaxyImage]) -> np.ndarray:
    temp_calc = TemperatureCalculator(images["U"], images["B"], images["V"])
    temp_image = temp_calc.compute_temperature_image()
    logging.info(f"Computed temperature image")

    unwinder = GalaxyUnwinder(temp_image)
    radial_data = unwinder.unwind()
    logging.info(f"Unwound radial data: {radial_data.shape}")

    averager = RadialAverager(radial_data)
    profile_data = averager.compute_average()
    return profile_data


def plot_temperature_profile(galaxy_name: str, profile_data: np.ndarray) -> None:
    profile = TemperatureProfile(profile_data)
    profile.plot_temperature(galaxy_name)
    logging.info(f"Plotted temperature profile for {galaxy_name}")


def main() -> None:
    loader = DataLoader()
    for galaxy_name, galaxy in loader.load_all_galaxies():
        process_galaxy(galaxy_name, galaxy)


if __name__ == "__main__":
    main()