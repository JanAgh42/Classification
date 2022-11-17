from ..constants.point_types import PointTypes
from .coordinates import Coordinates

class Point(Coordinates):

    def __init__(self, coords: tuple[int, int], type: PointTypes) -> None:
        super().__init__(coords)
        
        self.type = type
        self.distance = -1