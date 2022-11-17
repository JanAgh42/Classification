from ..constants.point_types import PointTypes
from ..models.point import Point

import random

class Misc:

    @staticmethod
    def get_random_coords(point_type: PointTypes) -> tuple[int, int]:
        percentage = random.random()

        if percentage > 0.99:
            return (random.randint(0, 9999), random.randint(0, 9999))
        
        match point_type:
            case PointTypes.BLUE:
                return (random.randint(0, 5499), random.randint(4500, 9999))
            case PointTypes.RED:
                return (random.randint(0, 5499), random.randint(0, 5499))
            case PointTypes.GREEN:
                return (random.randint(4500, 9999), random.randint(0, 5499))
            case _:
                return (random.randint(4500, 9999), random.randint(4500, 9999))

    @staticmethod
    def get_point_type(nearest_points: list[Point]) -> PointTypes:
        nearest_points_count = [0 for _ in range(4)]

        for value in nearest_points:
            nearest_points_count[value.type.value] += 1

        return PointTypes.get_point_types()[nearest_points_count.index(max(nearest_points_count))]

    @staticmethod
    def get_graph_color(point_type: PointTypes) -> str:
        match point_type:
            case PointTypes.BLUE:
                return 'blue'
            case PointTypes.RED:
                return 'red'
            case PointTypes.GREEN:
                return 'green'
            case _:
                return 'magenta'