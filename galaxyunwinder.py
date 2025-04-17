from galaxyimage import GalaxyImage
import numpy as np
import os

class GalaxyUnwinder:
    """
    Converts a galaxy image from Cartesian (x, y) to Polar (θ, r) coordinates.
    """

    def __init__(self, image: GalaxyImage) -> None:
        self.image: GalaxyImage = image
        self.center_x = self.image.shape[1] // 2
        self.center_y = self.image.shape[0] // 2
        self.max_radius = int(np.hypot(self.center_x, self.center_y))

    def unwind(self, num_angles: int = 360, num_radii: int = None) -> np.ndarray:
        """
        Unwinds the galaxy image into polar coordinates.
        Returns a 2D array of shape (num_angles, num_radii) representing the unwound image.
        """
        if num_radii is None:
            num_radii = self.max_radius

        polar_image = np.zeros((num_angles, num_radii))

        theta_vals = np.linspace(0, 2 * np.pi, num_angles, endpoint=False)
        r_vals = np.linspace(0, self.max_radius, num_radii)

        for i, theta in enumerate(theta_vals):
            for j, r in enumerate(r_vals):
                x = int(self.center_x + r * np.cos(theta))
                y = int(self.center_y + r * np.sin(theta))

                # Bounds check
                if 0 <= x < self.image.shape[1] and 0 <= y < self.image.shape[0]:
                    polar_image[i, j] = self.image[y, x]
                else:
                    polar_image[i, j] = np.nan

        return polar_image

    if __name__ == "__main__":
        import os
        import h5py
        import random
        import matplotlib.pyplot as plt
        from galaxyimage import GalaxyImage
        from galaxyunwinder import GalaxyUnwinder

        # Load the .h5 and pick an example image
        dataset = h5py.File("dataset/Galaxy10_DECals.h5", "r")
        data_images = [i for i, label in enumerate(dataset["ans"]) if label in (6, 7)]
        raw = dataset["images"][random.choice(data_images), :, :, 2]
        galaxy_image = GalaxyImage(raw)

        # Unwind and plot
        unwinder = GalaxyUnwinder(galaxy_image)
        polar = unwinder.unwind()

        plt.figure()
        plt.imshow(polar, aspect="auto", cmap="gray")
        plt.title("Polar Unwound Galaxy Image")
        plt.xlabel("Radius")
        plt.ylabel("Angle")
        plt.colorbar()
        plt.show()


