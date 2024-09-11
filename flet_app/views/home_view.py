import flet as ft
from i18n.language import language


def home_view(page: ft.Page):

    def change_language(e):
        selected_lang_code = dropdown.value
        language.set_language(selected_lang_code)
        page.clean()
        home_view(page)


    def update_checkbox(selected, checkboxes):
        for checkbox in checkboxes:
            if checkbox != selected:
                checkbox.value = False
        page.update()


    checkbox1 = ft.Checkbox(
        label=language.get("greeting"),
        value=False,
        on_change=lambda e: update_checkbox(
            checkbox1, [checkbox1, checkbox2, checkbox3]
        ),
    )
    checkbox2 = ft.Checkbox(
        label="Opcja 2",
        value=False,
        on_change=lambda e: update_checkbox(
            checkbox2, [checkbox1, checkbox2, checkbox3]
        ),
    )
    checkbox3 = ft.Checkbox(
        label="Opcja 3",
        value=False,
        on_change=lambda e: update_checkbox(
            checkbox3, [checkbox1, checkbox2, checkbox3]
        ),
    )


    dropdown_options = [
        ft.dropdown.Option(key=list(lang.values())[0], text=list(lang.keys())[0])
        for lang in language.supported_languages["languages"]
    ]

    current_language = language.language
    dropdown = ft.Dropdown(
        label=language.get("language"),
        options=dropdown_options, 
        value=current_language,
        on_change=change_language
    )

    page.add(
        ft.Row([dropdown], alignment=ft.MainAxisAlignment.END),
        ft.Text("Witaj w aplikacji Flet!" if language.language == "pl" else "Welcome to the Flet app!"),
        checkbox1,
        checkbox2,
        checkbox3
    )


ft.app(target=home_view)
