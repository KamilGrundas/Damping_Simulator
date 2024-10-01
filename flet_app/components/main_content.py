import flet as ft


class MainContent:
    def __init__(self, rectangle,spring, time_text):
        self.rectangle = rectangle
        self.time_text = time_text
        self.spring = spring
        self.view = self.create_main_content()

    def create_main_content(self):
        return ft.Container(
            content=ft.Stack(
                controls=[self.rectangle, self.spring, self.time_text],
                alignment=ft.alignment.top_center,
            ),
            expand=True,
            height=1000,
            bgcolor=ft.colors.LIGHT_GREEN,
            padding=10,
        )
