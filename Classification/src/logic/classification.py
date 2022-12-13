from ..constants.initial_points import all_initial_points
from ..constants.point_types import PointTypes
from ..constants import labels
from ..models.point import Point
from .output_creator import OutputCreator
from .miscellaneous import Misc

from timeit import default_timer as timer
from math import sqrt
import copy

class Classification:

    def __init__(self) -> None:
        self.output_creator = OutputCreator()

        self.map = [[False for _ in range(10000)] for _ in range(10000)]
        self.num_of_neighbors = [1, 3, 7, 15]

        self.generated_values = list()
        self.initial_values = list()

    def reset_lists(self) -> None:
        self.point_coords = {
            labels.RED_X: list(),
            labels.RED_Y: list(),
            labels.BLUE_X: list(),
            labels.BLUE_Y: list(),
            labels.GREEN_X: list(),
            labels.GREEN_Y: list(),
            labels.PURPLE_X: list(),
            labels.PURPLE_Y: list(),
        }
        self.current_values = copy.deepcopy(self.initial_values)
        
        self.total_num_of_points = 1
        self.guessed_num_of_points = 1

    def generate_initial_points(self) -> None:
        for point_type, collection in all_initial_points():
            for X, Y in collection:
                X += 5000
                Y += 5000
                
                self.map[Y][X] = True
                self.initial_values.append(Point(X, Y, point_type))

    def generate_new_points(self) -> None:
        for index in range(0, 1000):
            point_type = PointTypes.get_point_types()[index % 4]

            X, Y = self.generate_coords(point_type)

            self.map[Y][X] = True
            self.generated_values.append(Point(X, Y, point_type))

    def perform_classification(self) -> None:
        for neighbor in self.num_of_neighbors:
            self.reset_lists()
            start = timer()

            append = self.current_values.append

            for point in self.generated_values:
                found_point_type = self.classify(point.X, point.Y, neighbor)

                append(Point(point.X, point.Y, found_point_type))

                if point.type == found_point_type:
                    self.guessed_num_of_points += 1

                self.total_num_of_points += 1

            end = timer()
            self.generate_graph_data(neighbor, round(end - start, 2))

    def classify(self, x: int, y: int, neighbors: int) -> PointTypes:
        for point in self.current_values:
            point.distance = sqrt((point.X - x) ** 2 + (point.Y - y) ** 2)

        self.current_values.sort(key = lambda point : point.distance)

        return Misc.get_point_type(self.current_values[: neighbors])

    def generate_coords(self, point_type: PointTypes) -> tuple[int, int]:
        X, Y = 0, 0

        while True:
            X, Y = Misc.get_random_coords(point_type)

            if not self.map[Y][X]:
                break
        return (X, Y)

    def generate_graph_data(self, neighbor: int, time: float) -> None:
        for point in self.current_values: 
            X, Y = point.X, point.Y

            X -= 5000
            Y -= 5000

            match point.type:
                case PointTypes.RED:
                    self.point_coords[labels.RED_X].append(X)
                    self.point_coords[labels.RED_Y].append(Y)
                case PointTypes.GREEN:
                    self.point_coords[labels.GREEN_X].append(X)
                    self.point_coords[labels.GREEN_Y].append(Y)
                case PointTypes.BLUE:
                    self.point_coords[labels.BLUE_X].append(X)
                    self.point_coords[labels.BLUE_Y].append(Y)
                case _:
                    self.point_coords[labels.PURPLE_X].append(X)
                    self.point_coords[labels.PURPLE_Y].append(Y)

        self.output_creator.console_output(
            self.guessed_num_of_points, 
            self.total_num_of_points,
            time
        )
        self.output_creator.initialize_graph_settings(neighbor)
        self.output_creator.define_data(self.point_coords)
        self.output_creator.display_graph()