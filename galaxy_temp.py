#!/usr/bin/python

import numpy as np
import sys
import h5py
import os
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


def process_galaxy(galaxy_name: str, filepath: str) -> None:
    print(f"Processing galaxy: {galaxy_name}")

    try:
        galaxy_data = load_h5_galaxy(filepath)
        galaxy_location = find_galaxy_location(galaxy_data)
        filtered_images = mask_galaxy_images(galaxy_data, galaxy_location)

        if not all(f in filtered_images for f in ("R", "G", "Z")):
            sys.stderr.write(f"Error: Missing R, G, or Z filters for {galaxy_name}. Skipping...\n")
            return

        temperature_profile = compute_temperature_profile(filtered_images)
        plot_temperature_profile(galaxy_name, temperature_profile)

    except Exception as e:
        sys.stderr.write(f"Error processing galaxy {galaxy_name}: {str(e)}\n")
        sys.exit(1)


def load_h5_galaxy(filepath: str) -> dict:
    with h5py.File(filepath, 'r') as f:
        galaxy_data = {}
        for band in ['R', 'G', 'Z']:
            if band in f:
                galaxy_data[band] = f[band][()]
                print(f"Loaded {band}-band data")
    return galaxy_data


def find_galaxy_location(galaxy_data: dict) -> GalaxyLocation:
    wide_image = Image(galaxy_data['R'])  # Assume R band is widest
    galaxy_finder = GalaxyFinder(wide_image)
    location = galaxy_finder.find_galaxy()
    print(f"Found galaxy location at {location}")
    return location


def mask_galaxy_images(galaxy_data: dict, location: GalaxyLocation) -> dict[str, GalaxyImage]:
    images = {}
    for band, data in galaxy_data.items():
        image = Image(data)
        masker = GalaxyMasker(image, location)
        masked_image = GalaxyImage(masker.mask_out_galaxy())
        images[band] = masked_image
        print(f"Masked {band}-band image")
    return images


def compute_temperature_profile(images: dict[str, GalaxyImage]) -> np.ndarray:
    temp_calc = TemperatureCalculator(images["R"], images["G"], images["Z"])
    temp_image = temp_calc.compute_temperature_image()
    print("Computed temperature image")

    unwinder = GalaxyUnwinder(temp_image)
    radial_data = unwinder.unwind()
    print(f"Unwound radial data: {radial_data.shape}")

    averager = RadialAverager(radial_data)
    profile_data = averager.compute_average()
    return profile_data


def plot_temperature_profile(galaxy_name: str, profile_data: np.ndarray) -> None:
    profile = TemperatureProfile(profile_data)
    profile.plot_temperature(galaxy_name)
    print(f"Plotted temperature profile for {galaxy_name}")


def main() -> None:
    data_path = "./galaxy_data_h5/"  # Folder with .h5 files
    for filename in os.listdir(data_path):
        if filename.endswith(".h5"):
            galaxy_name = filename.split(".")[0]
            filepath = os.path.join(data_path, filename)
            process_galaxy(galaxy_name, filepath)


if __name__ == "__main__":
    main()