import numpy


class RadialAverager:
    def __init__(self, radial_data: numpy.ndarray) -> None:
        if radial_data.shape[0] != 360:
            print("Radial data must span 360 degrees.")
            raise ValueError

        self.radial_data: numpy.ndarray = radial_data

    def compute_average(self) -> list[float]:
        return [float(x) for x in numpy.nanmean(self.radial_data, 0)]
