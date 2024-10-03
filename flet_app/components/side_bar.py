import flet as ft
from i18n.language import language
from flet_app.classes.input_slider import SliderWithText
import json
import asyncio


class SideBar:
    def __init__(self, selected_vibration_type):
        self.selected_vibration_type = selected_vibration_type
        self.animation = None
        self.sliders_dict = {}
        self.load_config_and_create_sliders()
        self.view = self.create_side_bar()

    def load_config_and_create_sliders(self):
        with open("flet_app/views/widgets_config.json") as f:
            data = json.load(f)
        self.option_sliders = {}
        for vibration_type, controls in data.items():
            option_controls = []
            option_controls.append(
                ft.Text(value=language.get(vibration_type), style="titleMedium")
            )
            self.sliders_dict[vibration_type] = {}
            for control_name, control_data in controls.items():
                min_val = control_data["min"]
                max_val = control_data["max"]
                default_val = control_data["default_value"]
                slider_with_text = SliderWithText(
                    min_val, max_val, default_val, control_name
                )
                self.sliders_dict[vibration_type][control_name] = slider_with_text
                row = slider_with_text.create_row()
                option_controls.append(row)
            self.option_sliders[vibration_type] = option_controls

    def create_side_bar(self):
        start_button = ft.IconButton(
            icon=ft.icons.PLAY_CIRCLE_ROUNDED,
            icon_color=ft.colors.GREEN,
            icon_size=100,
            tooltip="Start",
            on_click=lambda e: asyncio.run(self.animation.timer.start()),
        )

        reset_button = ft.IconButton(
            icon=ft.icons.REPLAY_CIRCLE_FILLED_ROUNDED,
            icon_color=ft.colors.GREEN,
            icon_size=100,
            tooltip="Reset",
            on_click=lambda e: asyncio.run(self.animation.timer.reset()),
        )

        side_bar_top = ft.Container(
            content=ft.Row(
                controls=[
                    start_button,
                    reset_button,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            bgcolor=ft.colors.AMBER,
            padding=10,
        )

        self.side_bar_main = ft.Container(
            content=ft.Column(
                controls=self.option_sliders[self.selected_vibration_type], expand=True
            ),
            bgcolor=ft.colors.AMBER,
            padding=10,
            visible=True,
            expand=True,
        )

        return ft.Column(
            controls=[side_bar_top, self.side_bar_main],
            alignment=ft.MainAxisAlignment.START,
            expand=True,
        )

    def update_vibration_type(self, vibration_type):
        self.selected_vibration_type = vibration_type
        self.side_bar_main.content.controls = self.option_sliders[vibration_type]
        self.side_bar_main.content.update()
        self.view.update()
