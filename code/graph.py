import math
from matplotlib import pyplot as plt
from datetime import datetime


class Graph:
    def __init__(self, object):
        self.object = object
        self.draw_counter = 1
        self.clear_counter = 2
        self.x_1 = []
        self.y_1 = []
        self.x_2 = []
        self.y_2 = []
        self.x_3 = []
        self.y_3 = []

    def take_points(self, time):
        if self.draw_counter == 1:
            self.x_1.append(time)
            self.y_1.append(self.object.pos.y)
        elif self.draw_counter == 2:
            self.x_2.append(time)
            self.y_2.append(self.object.pos.y)
        elif self.draw_counter == 3:
            self.x_3.append(time)
            self.y_3.append(self.object.pos.y)

    def clear_points(self):
        if self.clear_counter == 4:
            print("Czyści 1")
            self.x_1 = []
            self.y_1 = []
            self.draw_counter = 1
            self.clear_counter += 1
        elif self.clear_counter == 5:
            print("Czyści 2")
            self.x_2 = []
            self.y_2 = []
            self.draw_counter = 2
            self.clear_counter += 1
        elif self.clear_counter == 6:
            print("Czyści 3")
            self.x_3 = []
            self.y_3 = []
            self.draw_counter = 3
            self.clear_counter = 4
        else:
            self.clear_counter += 1
            self.draw_counter += 1

    def show_graph(self, time):
        time_form = "%d.%m.%Y"

        all_y = self.y_1 + self.y_2 + self.y_3
        max_y = max(all_y)

        plt.rcParams["figure.figsize"] = [12.00, 3.50]
        plt.rcParams["figure.autolayout"] = True
        plt.figure(f"Wykres drgań {datetime.now().strftime(time_form)}")
        plt.title("Wykres drgań x(t)")
        plt.xlim(0, time)
        plt.xlabel("Czas t")
        plt.ylim(max_y + 0.5 * max_y, -max_y - 0.5 * max_y)
        plt.ylabel("Odchylenie x")
        plt.grid()
        plt.plot(
            self.x_1,
            self.y_1,
            marker="o",
            markersize=0.25,
            markeredgecolor="red",
            markerfacecolor="green",
        )
        plt.plot(
            self.x_2,
            self.y_2,
            marker="o",
            markersize=0.25,
            markeredgecolor="red",
            markerfacecolor="green",
        )
        plt.plot(
            self.x_3,
            self.y_3,
            marker="o",
            markersize=0.25,
            markeredgecolor="red",
            markerfacecolor="green",
        )
        plt.show()
