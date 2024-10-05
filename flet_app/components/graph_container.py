import flet as ft
import numpy as np
from flet_app.classes.animation import damped_vibrations


class Graph:
    def __init__(self, parameters):
        self.parameters = parameters
        self.line_chart = self.create_line_chart()

    def create_graph_data(self):
        time = np.linspace(0, 10, 5000)
        y_values = [damped_vibrations(t, self.parameters)[0] for t in time]

        extrema_indices = self.find_local_extrema(y_values)

        data_points = [
            ft.LineChartDataPoint(time[i], y_values[i]) for i in extrema_indices
        ]

        return data_points

    def find_local_extrema(self, y_values):
        extrema_indices = []

        if (y_values[0] > y_values[1]) or (y_values[0] < y_values[1]):
            extrema_indices.append(0)

        for i in range(1, len(y_values) - 1):
            if (y_values[i - 1] < y_values[i] > y_values[i + 1]) or (
                y_values[i - 1] > y_values[i] < y_values[i + 1]
            ):
                extrema_indices.append(i)

        if (y_values[-2] < y_values[-1]) or (y_values[-2] > y_values[-1]):
            extrema_indices.append(len(y_values) - 1)

        return extrema_indices

    def create_line_chart(self):
        data_points = self.create_graph_data()

        line_chart_data = ft.LineChartData(
            data_points=data_points,
            stroke_width=2,
            color=ft.colors.BLACK45,
            curved=True,
            stroke_cap_round=True,
        )

        line_chart = ft.LineChart(
            data_series=[line_chart_data],
            animate=ft.animation.Animation(100),
            min_x=0,
            max_x=10,
            min_y=min([dp.y for dp in data_points]),
            max_y=max([dp.y for dp in data_points]),
            expand=True,
            border=ft.border.all(1, ft.colors.with_opacity(0.2, ft.colors.ON_SURFACE)),
            horizontal_grid_lines=ft.ChartGridLines(
                interval=0.5,
                color=ft.colors.with_opacity(0.2, ft.colors.ON_SURFACE),
                width=1,
            ),
            vertical_grid_lines=ft.ChartGridLines(
                interval=1,
                color=ft.colors.with_opacity(0.2, ft.colors.ON_SURFACE),
                width=1,
            ),
            left_axis=ft.ChartAxis(
                labels=[
                    ft.ChartAxisLabel(
                        value=v,
                        label=ft.Text(f"{v:.1f}", size=12, weight=ft.FontWeight.BOLD),
                    )
                    for v in np.linspace(
                        min([dp.y for dp in data_points]),
                        max([dp.y for dp in data_points]),
                        5,
                    )
                ],
                labels_size=40,
            ),
            bottom_axis=ft.ChartAxis(
                labels=[
                    ft.ChartAxisLabel(
                        value=t,
                        label=ft.Text(f"{t:.0f}", size=12, weight=ft.FontWeight.BOLD),
                    )
                    for t in np.linspace(0, 10, 11)
                ],
                labels_size=32,
            ),
            tooltip_bgcolor=ft.colors.with_opacity(2, ft.colors.WHITE12),
        )

        return line_chart

    def view(self):
        return self.line_chart


class GraphContainer:
    def __init__(self):
        self.graph = None
        self.view = self.create_graph_container()

    def create_graph_container(self):
        return ft.Container(
            expand=True,
            height=700,
            bgcolor=ft.colors.LIGHT_BLUE,
            padding=10,
        )

    def update_graph(self, parameters):
        self.graph = Graph(parameters)
        self.view.content = self.graph.view()
        self.view.update()
