import numpy
import sys

from typing import Self, Any


class Image:
    """
    Image

    This represents a 2D helper class, providing multiple methods for image manipulation.

    Attribute:
        data (np.ndarray): 2D array of image data.
    """
    def __init__(self, data: numpy.ndarray) -> None:
        if len(data.shape) != 2:
            print("Error: Image data must be two-dimensional", file=sys.stderr)
            raise TypeError
        self._data: numpy.ndarray = data

    @property
    def data(self) -> numpy.ndarray:
        """
        Gets a numpy array of data from the image.

        Returns:
            numpy.ndarray: 2D array of image data.
        """
        return self._data

    @data.setter
    def data(self, value: Any) -> None:
        """
        Prevents against mutability of image data.

        Returns:
            TypeError: countermeasure against reassigning image data.
        """
        print("Error: Image data is not mutable.", file=sys.stderr)
        raise TypeError

    @property
    def shape(self) -> tuple[int, int]:
        """
        Find the shape of the image.

        Returns:
            tuple[int, int]: Shape of image data.
        """
        return (self.data.shape[0], self.data.shape[1])

    def mean(self) -> float:
        """
        Compute the mean of the image data(omit NaNs).

        Returns:
            float: Mean of image data.
        """
        return numpy.nanmean(self.data)

    def median(self) -> float:
        """
        Find the median of image data(omit NaNs).

        Returns:
            float: Median of image data.
        """
        return numpy.nanmedian(self.data)

    def std(self) -> float:
        """
        Compute the standard deviation of the image data(omit NaNs).

        Returns:
            float: Standard deviation of image data.
        """
        return numpy.nanstd(self.data)

    def scale(self, num: float | int) -> Self:
        """
        Scales the image with a dividing factor.

        Parameter:
            num (float): Scaling factor.

        Returns:
            Image with scaled image data.
        """
        return type(self)(self.data / num)

    def rot_right(self) -> Self:
        """
        Rotates an image 90 degrees.

        Returns:
            Image: 90 degree rotated image.
        """
        return type(self)(numpy.rot90(self.data))

    def rot_left(self) -> Self:
        """
        Rotates an image counterclockwise by 90 degrees.

        Returns:
            Image: counter-clockwise 90 degree rotated image.
        """
        return type(self)(
            numpy.rot90(self.data, 3)
        )  # Rotate 90 degrees 3 times -> 270 degrees

    def __getitem__(self, key: tuple[slice, slice]) -> float | numpy.ndarray:
        """
        Accesses a smaller region of the image.

        Parameter:
            key (tuple): 2 slice indices for x and y coordinates.

        Returns:
            float | numpy.ndarray: the given subregion of the image.
        """
        if len(key) != 2:
            print("Error: Images must be accessed in two dimensions.")
            raise ValueError

        return self.data[key]

    def __add__(self, other) -> Self:
        """
        Adds two images values.
        Parameter:
            other (Image): Image to add.

        Returns:
            Image: Sum of two images values.
        """
        if not isinstance(other, Image):
            print("Error: Images can only be added with other images.")
            raise TypeError

        return type(self)(self.data + other.data)

    def __radd__(self, other) -> None:
        """
        Returns:
            TypeError: can only add images with other images.
        """
        print("Error: Images can only be added with other images.")
        raise TypeError

    def __sub__(self, other) -> Self:
        """
        Subtracts two images values.

        Parameter:
            other (Image): Image to subtract.

        Returns:
            Image: Difference of two images values.
        """
        if not isinstance(other, Image):
            print("Error: Images can only be subtracted with other images.")
            raise TypeError

        return type(self)(self.data - other.data)

    def __rsub__(self, other) -> None:
        """
        Returns:
            TypeError: can only subtract images with other images.
        """
        print("Error: Images can only be subtracted with other images.")
        raise TypeError

    def __mul__(self, other) -> Self:
        """
        Multiplies two images values.

        Attribute:
            other (Image): Image to multiply.

        Returns:
            Image: Product of two images values.
        """
        if not isinstance(other, Image):
            print("Error: Images can only be multiplied with other images.")
            raise TypeError

        return type(self)(self.data * other.data)

    def __rmul__(self, other) -> None:
        """
        Returns:
            TypeError: can only multiply images with other images.
        """
        print("Error: Images can only be multiplied with other images.")
        raise TypeError

    def __div__(self, other) -> Self:
        """
        Divides two images values.

        Parameter:
            other (Image): Image to divide.

        Returns:
            Image: Quotient of two images values.
        """
        if not isinstance(other, Image):
            print("Error: Images can only be divided with other images.")
            raise TypeError

        return type(self)(self.data / other.data)

    def __rdiv__(self, other) -> None:
        """
        Returns:
            TypeError: can only divide images with other images.
        """
        print("Error: Images can only be divided with other images.")
        raise TypeError
