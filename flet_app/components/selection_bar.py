import flet as ft
from i18n.language import language


class SelectionBar:
    def __init__(self, on_language_change, on_vibration_type_change):
        self.language_dropdown = self.create_language_dropdown(on_language_change)
        self.vibration_type_dropdown = self.create_vibration_dropdown(
            on_vibration_type_change
        )
        self.view = self.create_navigation_bar()

    def create_language_dropdown(self, on_language_change):
        dropdown_options = [
            ft.dropdown.Option(key=list(lang.values())[0], text=list(lang.keys())[0])
            for lang in language.supported_languages["languages"]
        ]
        current_language = language.language
        return ft.Dropdown(
            label=language.get("language"),
            options=dropdown_options,
            value=current_language,
            on_change=on_language_change,
        )

    def create_vibration_dropdown(self, on_vibration_type_change):
        dropdown_options = [
            ft.dropdown.Option(
                key="damped_vibrations", text=language.get("damped_vibrations")
            ),
            ft.dropdown.Option(
                key="forced_damped_vibrations",
                text=language.get("forced_damped_vibrations"),
            ),
            ft.dropdown.Option(
                key="dynamic_vibration_absorber",
                text=language.get("dynamic_vibration_absorber"),
            ),
        ]

        return ft.Dropdown(
            label=language.get("select_vibration_type"),
            options=dropdown_options,
            value="damped_vibrations",
            on_change=on_vibration_type_change,
        )

    def create_navigation_bar(self):
        return ft.Container(
            content=ft.Row(
                controls=[
                    self.vibration_type_dropdown,
                    ft.Text(
                        value="Damped vibrations simulator", size=30, color="#2efad8"
                    ),
                    self.language_dropdown,
                ],
                alignment="spaceBetween",
            ),
            height=70,
            border_radius=10,
            bgcolor="#0c1d2c",
            padding=ft.padding.only(top=10, left=10, right=10),
        )
