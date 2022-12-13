from ..constants.point_types import PointTypes
from ..constants import labels
from .miscellaneous import Misc

from matplotlib import pyplot as plt

class OutputCreator:

    def initialize_graph_settings(self, neighbor: int) -> None:
        self.ax = plt.figure().add_subplot(1, 1, 1)

        self.ax.spines['left'].set_position('zero')
        self.ax.spines['bottom'].set_position('zero')

        self.ax.spines['right'].set_color('none')
        self.ax.spines['top'].set_color('none')

        self.ax.xaxis.set_ticks_position('bottom')
        self.ax.yaxis.set_ticks_position('left')

        plt.title(f'Value of k: { neighbor }')

    def define_data(self, data: dict[str, list[int]]) -> None:
        self.plot_data(data[labels.RED_X], data[labels.RED_Y], PointTypes.RED)
        self.plot_data(data[labels.BLUE_X], data[labels.BLUE_Y], PointTypes.BLUE)
        self.plot_data(data[labels.GREEN_X], data[labels.GREEN_Y], PointTypes.GREEN)
        self.plot_data(data[labels.PURPLE_X], data[labels.PURPLE_Y], PointTypes.PURPLE)

    def plot_data(self, data_x: list, data_y: list, point_type: PointTypes) -> None:
        color = Misc.get_graph_color(point_type)

        plt.scatter(data_x, data_y, color = color)

    def display_graph(self) -> None:
        plt.show()

    def console_output(self, guessed: int, total: int, time: float) -> None:
        print('**********************************************')
        print(f'Effectivity: { (guessed / total) * 100 }%')
        print(f'Time: { time }s')
        print('**********************************************')