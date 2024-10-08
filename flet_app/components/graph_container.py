import flet as ft
from flet_app.classes.graph import graph



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
            content=graph.view()
        )

    def update_graph(self):
        self.view.content = graph.view()
        self.view.update()
