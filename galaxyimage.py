from image import Image
import numpy


class GalaxyImage(Image):
    """
    GalaxyImage

    This class creates an object that provides the center and radius,
    making it a large help for further work.

    Attribute:
        image (Image): Image object containing galaxy data.
    """

    def __init__(self, image: Image) -> None:
        """
        Initialize a GalaxyImage object from a previous image.
        Args:
            image (Image): input Image object to use for extraction.
        """
        super().__init__(image.data)

    @property
    def center(self) -> tuple[float, float]:
        """
        Returns:
            tuple: (x, y) coordinates of the image center
        """
        return (self.shape[0] // 2, self.shape[1] // 2)

    @property
    def radius(self) -> float:
        """
        Returns:
            float: radius of the image of the shapes diagonal multiplied by 2.
        """
        return 2 * numpy.sqrt(self.shape[0] ** 2 + self.shape[1] ** 2)
