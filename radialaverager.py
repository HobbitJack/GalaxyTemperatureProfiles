import numpy


class RadialAverager:
    """
    RadialAverager

    Computes average value for each radius across angles in a polar image.

    Attributes:
        radial_data (numpy.ndarray): 2D array of radial data,
        containing angles in the rows, and radii in the columns.
    """

    def __init__(self, radial_data: numpy.ndarray) -> None:
        if radial_data.shape[0] != 360:
            print("Radial data must span 360 degrees.")
            raise ValueError

        self.radial_data: numpy.ndarray = radial_data

    def compute_average(self) -> list[float]:
        """
        Computes average value for each radius across all angles.

        Returns:
            list[float]: Average radial values for each position.
        """
        return [float(x) for x in numpy.nanmean(self.radial_data, 0)]
