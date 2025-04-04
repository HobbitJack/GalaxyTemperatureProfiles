import numpy
import sys

from typing import Self, Any


class Image:
    def __init__(self, data: numpy.ndarray) -> None:
        if len(data.shape) != 2:
            print("Error: Image data must be two-dimensional", file=sys.stderr)
            raise TypeError
        self._data: numpy.ndarray = data

    @property
    def data(self) -> numpy.ndarray:
        return self._data

    @data.setter
    def data(self, value: Any) -> None:
        print("Error: Image data is not mutable.", file=sys.stderr)
        raise TypeError

    @property
    def shape(self) -> tuple[int, int]:
        return (self.data.shape[0], self.data.shape[1])

    def mean(self) -> float:
        return numpy.nanmean(self.data)

    def median(self) -> float:
        return numpy.nanmedian(self.data)

    def std(self) -> float:
        return numpy.nanstd(self.data)

    def scale(self, num: float | int) -> Self:
        return type(self)(self.data / num)

    def rot_right(self) -> Self:
        return type(self)(numpy.rot90(self.data))

    def rot_left(self) -> Self:
        return type(self)(
            numpy.rot90(self.data, 3)
        )  # Rotate 90 degrees 3 times -> 270 degrees

    def __getitem__(self, key: tuple[slice, slice]) -> float | numpy.ndarray:
        if len(key) != 2:
            print("Error: Images must be accessed in two dimensions.")
            raise ValueError

        return self.data[key]

    def __add__(self, other) -> Self:
        if not isinstance(other, Image):
            print("Error: Images can only be added with other images.")
            raise TypeError

        return type(self)(self.data + other.data)

    def __radd__(self, other) -> None:
        print("Error: Images can only be added with other images.")
        raise TypeError

    def __sub__(self, other) -> Self:
        if not isinstance(other, Image):
            print("Error: Images can only be subtracted with other images.")
            raise TypeError

        return type(self)(self.data - other.data)

    def __rsub__(self, other) -> None:
        print("Error: Images can only be subtracted with other images.")
        raise TypeError

    def __mul__(self, other) -> Self:
        if not isinstance(other, Image):
            print("Error: Images can only be multiplied with other images.")
            raise TypeError

        return type(self)(self.data * other.data)

    def __rmul__(self, other) -> None:
        print("Error: Images can only be multiplied with other images.")
        raise TypeError

    def __div__(self, other) -> Self:
        if not isinstance(other, Image):
            print("Error: Images can only be divided with other images.")
            raise TypeError

        return type(self)(self.data / other.data)

    def __rdiv__(self, other) -> None:
        print("Error: Images can only be divided with other images.")
        raise TypeError
