class Coordinates:

    def __init__(self, coords: tuple[int, int]) -> None:
        self.update_coords(coords)

    def update_coords(self, coords: tuple[int, int]) -> None:
        self.X, self.Y = coords

    def get_coords(self) -> tuple[int, int]:
        return (self.X, self.Y)