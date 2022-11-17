from src.logic.classification import Classification
from src.logic.output_creator import OutputCreator

from src.constants.point_types import PointTypes

classification = Classification()
output_creator = OutputCreator()

classification.generate_initial_points()
classification.generate_new_points(3)
classification.generate_graph_data()

output_creator.plot_data(
    classification.blue_point_coords_x,
    classification.blue_point_coords_y,
    PointTypes.BLUE)

output_creator.plot_data(
    classification.red_point_coords_x,
    classification.red_point_coords_y,
    PointTypes.RED)

output_creator.plot_data(
    classification.green_point_coords_x,
    classification.green_point_coords_y,
    PointTypes.GREEN)

output_creator.plot_data(
    classification.purple_point_coords_x,
    classification.purple_point_coords_y,
    PointTypes.PURPLE)

output_creator.display_graph()

print(classification.guessed_num_of_points / classification.total_num_of_points)