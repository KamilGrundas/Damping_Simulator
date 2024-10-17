import flet as ft


class AnimationContainer:
    def __init__(self, rectangle, spring, rectangle2, spring2, time_text):
        self.rectangle = rectangle
        self.rectangle2 = rectangle2
        self.time_text = time_text
        self.spring = spring
        self.spring2 = spring2
        self.view = self.create_animation_container()

    def create_animation_container(self):
        animation_content = ft.Stack(
            controls=[
                self.rectangle,
                self.spring,
                self.rectangle2,
                self.spring2,
                self.time_text,
            ],
            alignment=ft.alignment.top_center,
            expand=True,
        )

        return ft.Container(
            content=animation_content,
            expand=True,
            bgcolor=ft.colors.WHITE,
            padding=10,
            border_radius=10,
        )
