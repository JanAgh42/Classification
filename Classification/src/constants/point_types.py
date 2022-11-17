from enum import Enum

class PointTypes(Enum):
    RED = 0
    GREEN = 1
    BLUE = 2
    PURPLE = 3

    @classmethod
    def get_point_types(cls) -> list:
        return [
            cls.RED,
            cls.GREEN,
            cls.BLUE,
            cls.PURPLE
        ]