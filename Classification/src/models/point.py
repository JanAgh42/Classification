from ..constants.point_types import PointTypes

class Point:

    __slots__ =  ['X', 'Y', 'type', 'distance']

    def __init__(self, x: int, y: int, type: PointTypes) -> None:
        self.X = x
        self.Y = y
        self.type = type
        self.distance = -1