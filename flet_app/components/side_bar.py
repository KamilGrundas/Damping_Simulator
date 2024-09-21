import flet as ft
from i18n.language import language
from flet_app.classes.input_slider import SliderWithText
import json


class SideBar:
    def __init__(self):
        self.sliders_dict = {}
        self.load_config_and_create_sliders()
        self.view = self.create_side_bar()

    def load_config_and_create_sliders(self):
        with open("flet_app/views/widgets_config.json") as f:
            data = json.load(f)
        self.option_sliders = {}
        for index, (level_name, controls) in enumerate(data.items()):
            option_controls = []
            option_controls.append(
                ft.Text(value=language.get(level_name), style="titleMedium")
            )
            self.sliders_dict[level_name] = {}
            for control_name, control_data in controls.items():
                min_val = control_data["min"]
                max_val = control_data["max"]
                default_val = control_data["default_value"]
                slider_with_text = SliderWithText(
                    min_val, max_val, default_val, control_name
                )
                self.sliders_dict[level_name][control_name] = slider_with_text
                row = slider_with_text.create_row()
                option_controls.append(row)
            self.option_sliders[str(index)] = option_controls

    def create_side_bar(self):

        self.radio_group = ft.RadioGroup(
            content=ft.Column(
                [
                    ft.Radio(value="0", label=language.get("damped_vibrations")),
                    ft.Radio(value="1", label=language.get("forced_damped_vibrations")),
                    ft.Radio(
                        value="2", label=language.get("dynamic_vibration_absorber")
                    ),
                ]
            ),
            value="0",
            on_change=self.radio_group_changed,
        )

        side_bar_top = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(
                        value=language.get("type_of_vibration"), style="titleLarge"
                    ),
                    self.radio_group,
                ]
            ),
            width=400,
            bgcolor=ft.colors.AMBER,
            padding=10,
        )

        self.side_bar_main = ft.Container(
            content=ft.Column(controls=self.option_sliders["0"]),
            width=400,
            bgcolor=ft.colors.AMBER,
            padding=10,
            visible=True,
        )

        return ft.Column(
            controls=[side_bar_top, self.side_bar_main],
            alignment=ft.MainAxisAlignment.START,
        )

    def radio_group_changed(self, e):
        selected_value = self.radio_group.value
        controls = self.option_sliders.get(selected_value, [])
        self.side_bar_main.content.controls = controls
        self.side_bar_main.content.update()
        self.view.update()
