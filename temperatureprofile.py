import matplotlib.pyplot as plt
import numpy as np

"""
TemperatureProfile

This class handles plotting of a galaxy's radial temperature profile.

The input is a 1D array of temperature values (in Kelvin) averaged over radial bins.
The x-axis represents normalized radial distance (from galaxy center to edge).
The y-axis shows effective temperature in Kelvin.

The plot is saved as a .png image in the output directory.
"""

class TemperatureProfile:
    def __init__(self, temperature_data: list[float]) -> None:
        self.temperature_data = temperature_data

    def plot_temperature(self, galaxy_name: str) -> None:
        plt.figure(figsize=(8, 10))
        plt.plot(np.linspace(0, 1, len(self.temperature_data)), self.temperature_data)
        plt.xlabel("Radial Distance (Normalized to Galaxy Radius)")
        plt.ylabel("Effective Temperature (Kelvin)")
        plt.title(f"Temperature Profile of Galaxy {galaxy_name}")
        plt.savefig(f"output/{galaxy_name}.png")