import numpy
import sys

from typing import Self


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
    def data(self, value: any) -> None:
        print("Error: Image data is not mutable.", file=sys.stderr)
        raise TypeError

    @property
    def shape(self) -> tuple[int, int]:
        return (self.data.shape[1], self.data.shape[0])

    def mean(self) -> float:
        return numpy.nanmean(self.data)

    def median(self) -> float:
        return numpy.nanmedian(self.data)

    def std(self) -> float:
        return numpy.nanstd(self.data)

    def scale(self, num: float | int) -> Self:
        return Image(self.data / num)

    def rot_right(self) -> Self:
        return Image(numpy.rot90(self.data))

    def rot_left(self) -> Self:
        return Image(
            numpy.rot90(self.data, 3)
        )  # Rotate 90 degrees 3 times -> 270 degrees

    def get_array_index(self, *coord) -> tuple[int, int]:
        if len(coord) == 1:
            x, y = *coord
        else:
            x, y = coord

        return (y - self.shape[1], x)

    def __getitem__(self, key: tuple[slice, slice]) -> float:
        if len(key) != 2:
            print("Error: Images must be accessed in two dimensions.")
            raise ValueError

        x_slice, y_slice = key
        return Image(
            self.data[
                slice(
                    None if y_slice.stop is None else (self.shape[1] - y_slice.stop),
                    None if y_slice.start is None else (self.shape[1] - y_slice.start),
                    y_slice.step,
                )
            ][x_slice]
        )

    def get(self, x, y) -> float:
        return self.data[self.shape[1] - y][x]

    def __add__(self, other) -> Self:
        if not isinstance(other, Image):
            print("Error: Images can only be added with other images.")
            raise TypeError

        return Image(self.data + other.data)

    def __radd__(self, other) -> None:
        print("Error: Images can only be added with other images.")
        raise TypeError

    def __sub__(self, other) -> Self:
        if not isinstance(other, Image):
            print("Error: Images can only be subtracted with other images.")
            raise TypeError

        return Image(self.data - other.data)

    def __rsub__(self, other) -> None:
        print("Error: Images can only be subtracted with other images.")
        raise TypeError

    def __mul__(self, other) -> Self:
        if not isinstance(other, Image):
            print("Error: Images can only be multiplied with other images.")
            raise TypeError

        return Image(self.data * other.data)

    def __rmul__(self, other) -> None:
        print("Error: Images can only be multiplied with other images.")
        raise TypeError

    def __div__(self, other) -> Self:
        if not isinstance(other, Image):
            print("Error: Images can only be divided with other images.")
            raise TypeError

        return Image(self.data / other.data)

    def __rdiv__(self, other) -> None:
        print("Error: Images can only be divided with other images.")
        raise TypeError
