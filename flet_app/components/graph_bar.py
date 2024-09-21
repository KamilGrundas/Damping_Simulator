import flet as ft
import numpy as np
import matplotlib.pyplot as plt
from flet.matplotlib_chart import MatplotlibChart
from flet_app.classes.animation import damped_vibrations


class GraphBar:
    def __init__(self):
        self.view = self.create_graph_bar()

    def create_graph_bar(self):
        return ft.Container(
            content=ft.Text(value="Graph Bar", style="titleMedium"),
            height=700,
            bgcolor=ft.colors.LIGHT_BLUE,
            padding=10,
        )

    def update_graph(self, parameters):
        fig, ax = plt.subplots()
        time = np.linspace(0, 10, 10000)
        y_values = [damped_vibrations(t, parameters)[0] for t in time]
        ax.plot(time, y_values)
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Amplitude")
        ax.legend(title="Damped Vibrations")
        self.view.content = MatplotlibChart(fig, expand=True)
        self.view.update()
