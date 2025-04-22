"""
galaxyunwinder.py

This module defines the GalaxyUnwinder class, which transforms a GalaxyImage from
Cartesian (x, y) coordinates to a polar (θ, r) representation using the largest
inscribed circle radius to guarantee in-bounds sampling. An example under the
__main__ guard demonstrates its usage for visualization.
"""

from galaxyimage import GalaxyImage
import numpy as np
import os


class GalaxyUnwinder:
    """
    Unwraps a GalaxyImage from Cartesian to polar coordinates.

    Attributes:
        image (GalaxyImage): The input galaxy image array (height × width).
        center_x (int): X-coordinate of the image center.
        center_y (int): Y-coordinate of the image center.
        max_radius (int): Inscribed circle radius ensuring all samples stay in-bounds.
    """

    def __init__(self, image: GalaxyImage) -> None:
        """
        Initialize the GalaxyUnwinder with a GalaxyImage instance.

        Args:
            image (GalaxyImage): Grayscale image array to be unwound.
        """
        self.image = image
        self.center_x = image.shape[1] // 2
        self.center_y = image.shape[0] // 2
        # Inscribed circle radius (distance to nearest image edge)
        self.max_radius = min(self.center_x, self.center_y)

    def unwind(self, num_angles: int = 360, num_radii: int = None) -> np.ndarray:
        """
        Convert the image from Cartesian (x, y) to polar (θ, r) coordinates.

        Args:
            num_angles (int, optional): Number of angular samples (default: 360).
            num_radii (int, optional): Number of radial samples. If None,
                uses the maximum radius (self.max_radius).

        Returns:
            np.ndarray: 2D array of shape (num_angles, num_radii) where each row
            corresponds to a fixed angle and each column to a radius from center.
        """
        if num_radii is None:
            num_radii = self.max_radius

        polar_image = np.zeros((num_angles, num_radii))
        theta_vals = np.linspace(0, 2 * np.pi, num_angles, endpoint=False)
        # exclude the endpoint to avoid r == max_radius exactly
        r_vals = np.linspace(0, self.max_radius, num_radii, endpoint=False)

        for i, theta in enumerate(theta_vals):
            for j, r in enumerate(r_vals):
                x = int(self.center_x + r * np.cos(theta))
                y = int(self.center_y + r * np.sin(theta))

                # Guaranteed in-bounds since r < max_radius and max_radius <= half-dimension
                polar_image[i, j] = self.image[y, x]

        return polar_image


if __name__ == "__main__":
    """
    Example usage:
    Load an HDF5 dataset of galaxy images, select labeled examples,
    apply the unwinder, and display the polar-transformed image.
    """
    import h5py
    import random
    import matplotlib.pyplot as plt

    # Load dataset and select galaxies with labels 6 or 7
    dataset = h5py.File("dataset/Galaxy10_DECals.h5", "r")
    data_images = [i for i, label in enumerate(dataset["ans"]) if label in (6, 7)]
    raw = dataset["images"][random.choice(data_images), :, :, 2]
    galaxy_image = GalaxyImage(raw)

    # Perform unwinding and visualize
    unwinder = GalaxyUnwinder(galaxy_image)
    polar = unwinder.unwind()
    polar_T = polar.T  # Transpose to (radii, angles) for bottom-up display

    plt.figure()
    plt.imshow(polar_T, aspect="auto", cmap="gray", origin="lower")
    plt.title("Polar Unwound Galaxy Image (Inscribed Radius)")
    plt.xlabel("Angle")
    plt.ylabel("Radius")
    plt.colorbar()
    plt.show()
