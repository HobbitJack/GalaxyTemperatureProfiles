class GalaxyLocation:
    """
    Galaxylocation

    Stores the center and radius for a galaxy in an image.

    Attributes:
        center (tuple[int, int]): center of galaxy in (x, y) format.
        radius (int): radius of galaxy region.
    """
    def __init__(self, center: tuple[int, int], radius: int) -> None:
        self.center: tuple[int, int] = center
        self.radius: int = radius
