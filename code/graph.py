import math
from matplotlib import pyplot as plt
from datetime import datetime


class Graph:
    def __init__(self, object):
        self.object = object
        self.x = []
        self.y = []

    def take_points(self, time):
        self.x.append(time)
        self.y.append(self.object.pos.y)

    def show_graph(self, time):
        time_form = "%d.%m.%Y"

        plt.rcParams["figure.figsize"] = [12.00, 3.50]
        plt.rcParams["figure.autolayout"] = True
        plt.figure(f"Wykres drgań {datetime.now().strftime(time_form)}")
        plt.title("Wykres drgań x(t)")
        plt.xlim(0, time)
        plt.xlabel("Czas t")
        plt.ylim(-2, 2)
        plt.ylabel("Odchylenie x")
        plt.grid()
        plt.plot(
            self.x,
            self.y,
            marker="o",
            markersize=1,
            markeredgecolor="red",
            markerfacecolor="green",
        )
        plt.show()
