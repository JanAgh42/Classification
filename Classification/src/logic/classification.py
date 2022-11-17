from ..constants.initial_points import all_initial_points
from ..constants.point_types import PointTypes
from ..models.point import Point
from .miscellaneous import Misc

import math

class Classification:

    def __init__(self) -> None:
        self.map = [[None for _ in range(10000)] for _ in range(10000)]

        self.recorded_values = list()

        self.red_point_coords_x = list()
        self.red_point_coords_y = list()

        self.blue_point_coords_x = list()
        self.blue_point_coords_y = list()

        self.green_point_coords_x = list()
        self.green_point_coords_y = list()

        self.purple_point_coords_x = list()
        self.purple_point_coords_y = list()

        self.total_num_of_points = 0
        self.guessed_num_of_points = 0

        self.counter = 0

    def generate_initial_points(self) -> list:
        for point_type, collection in all_initial_points():
            for X, Y in collection:
                X += 5000
                Y += 5000

                init_point = Point((X, Y), point_type)

                self.map[Y][X] = init_point
                self.recorded_values.append(init_point)

    def generate_new_points(self, neighbors: int) -> None:
        for index in range(0, 5000):
            point_type = PointTypes.get_point_types()[index % 4]

            X, Y = self.generate_coords(point_type)

            found_point_type = self.classify((X, Y), neighbors)

            new_point = Point((X, Y), found_point_type)

            self.map[Y][X] = new_point
            self.recorded_values.append(new_point)

            self.compare_results(point_type, found_point_type)
            print(self.counter)
            self.counter += 1

    def classify(self, coords: tuple[int, int], neighbors: int) -> PointTypes:
        X, Y = coords
        
        def sort_func(point: Point) -> float:
            return point.distance

        for point in self.recorded_values:
            point_x, point_y = point.get_coords()

            point.distance = math.sqrt((point_x - X) ** 2 + (point_y - Y) ** 2)

        self.recorded_values.sort(key = sort_func)

        return Misc.get_point_type(self.recorded_values[: neighbors])

    def compare_results(self, set_point_type: PointTypes, got_point_type: PointTypes) -> None:
        if set_point_type == got_point_type:
            self.guessed_num_of_points += 1

        self.total_num_of_points += 1

    def generate_coords(self, point_type: PointTypes) -> tuple[int, int]:
        X, Y = 0, 0

        while True:
            X, Y = Misc.get_random_coords(point_type)

            if self.map[Y][X] == None:
                break
        return (X, Y)

    def generate_graph_data(self) -> None:
        for point in self.recorded_values:
            X, Y = point.get_coords()

            X -= 5000
            Y -= 5000

            match point.type:
                case PointTypes.RED:
                    self.red_point_coords_x.append(X)
                    self.red_point_coords_y.append(Y)
                case PointTypes.GREEN:
                    self.green_point_coords_x.append(X)
                    self.green_point_coords_y.append(Y)
                case PointTypes.BLUE:
                    self.blue_point_coords_x.append(X)
                    self.blue_point_coords_y.append(Y)
                case _:
                    self.purple_point_coords_x.append(X)
                    self.purple_point_coords_y.append(Y)