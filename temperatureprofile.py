import matplotlib.pyplot as plt
import numpy as np


class TemperatureProfile:
    def __init__(self, temperature_data: list[float]) -> None:
        self.temperature_data = temperature_data

    def plot_temperature(self, galaxy_name: str) -> None:
        plt.figure(figsize=(8, 10))
        plt.plot(np.linspace(0, 1, len(self.temperature_data)), self.temperature_data)
        plt.xlabel("Radial Distance (Normalized to Galaxy Radius)")
        plt.ylabel("Effective Color Temperature")
        plt.title(f"Temperature Profile of Galaxy {galaxy_name}")
        plt.savefig(f"output/{galaxy_name}.png")