class GalaxyLocation:
    def __init__(self, center: tuple[int, int], radius: int) -> None:
        self.center: tuple[int, int] = center
        self.radius: int = radius
