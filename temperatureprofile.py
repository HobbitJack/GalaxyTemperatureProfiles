import matplotlib.pyplot
import numpy


class TemperatureProfile:
    def __init__(self, data: list[float]) -> None:
        self.temperature_data: list[float] = data

    def plot_temperature(self, file_prefix="Temperature") -> None:
        matplotlib.pyplot.plot(
            numpy.linspace(0, 1, len(self.temperature_data)), self.temperature_data
        )
        matplotlib.pyplot.xlabel("Radial Distance (Normalized to Galaxy Radius)")
        matplotlib.pyplot.ylabel("Effective Color Temperature")
        matplotlib.pyplot.title(f"Temperature Profile of {file_prefix}")
        matplotlib.pyplot.savefig(fname=f"output/{file_prefix}.png")
