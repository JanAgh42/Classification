from ..constants.point_types import PointTypes
from .miscellaneous import Misc

from matplotlib import pyplot as plt

class OutputCreator:

    def __init__(self) -> None:
        self.ax = plt.figure().add_subplot(1, 1, 1)

        self.ax.spines['left'].set_position('zero')
        self.ax.spines['bottom'].set_position('zero')

        self.ax.spines['right'].set_color('none')
        self.ax.spines['top'].set_color('none')

        self.ax.xaxis.set_ticks_position('bottom')
        self.ax.yaxis.set_ticks_position('left')

    def plot_data(self, data_x: list, data_y: list, point_type: PointTypes) -> None:
        color = Misc.get_graph_color(point_type)

        plt.scatter(data_x, data_y, color = color)

    def display_graph(self) -> None:
        plt.show()