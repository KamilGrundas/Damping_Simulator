import flet as ft
from i18n.language import language


class NavigationBar:
    def __init__(self, on_language_change):
        self.dropdown = self.create_language_dropdown(on_language_change)
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

    def create_navigation_bar(self):
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Text(
                        value="Navigation Bar",
                        style="headlineSmall",
                    ),
                    self.dropdown,
                ],
                alignment="spaceBetween",
            ),
            height=70,
            bgcolor=ft.colors.BLUE,
            padding=10,
        )
