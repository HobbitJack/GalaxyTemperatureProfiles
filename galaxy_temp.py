from dataloader import DataLoader
from galaxyfinder import GalaxyFinder
from galaxyimage import GalaxyImage
from galaxylocation import GalaxyLocation
from galaxymasker import GalaxyMasker


def main() -> None:
    data_loader: DataLoader = DataLoader()
    for galaxy in data_loader.load_all_galaxies():
        for filt, image in galaxy.load_all_images():
            galaxy_finder: GalaxyFinder = GalaxyFinder(image)
            galaxy_location: GalaxyLocation = galaxy_finder.find_galaxy()


if __name__ == "__main__":
    main()
