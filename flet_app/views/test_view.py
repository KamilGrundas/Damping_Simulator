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
        label="Opcja 1",
        value=False,
        on_change=lambda e: update_checkbox(checkbox1, [checkbox1, checkbox2, checkbox3]),
    )
    checkbox2 = ft.Checkbox(
        label="Opcja 2",
        value=False,
        on_change=lambda e: update_checkbox(checkbox2, [checkbox1, checkbox2, checkbox3]),
    )
    checkbox3 = ft.Checkbox(
        label="Opcja 3",
        value=False,
        on_change=lambda e: update_checkbox(checkbox3, [checkbox1, checkbox2, checkbox3]),
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

    nav_bar = ft.Container(
        content=ft.Row(
            controls=[
                ft.Text(
                    value="Navigation Bar",
                    style="headlineSmall",
                ),
                ft.Dropdown(
                    options=dropdown_options,
                    value=current_language,
                    on_change=change_language,
                ),
            ],
            alignment="spaceBetween",
        ),
        height=100,
        bgcolor=ft.colors.BLUE,
        padding=10,
    )


    main = ft.Container(
        content=ft.Text(
            value="Main Content",
            style="titleLarge"
        ),
        height=300,
        expand=True,
        bgcolor=ft.colors.LIGHT_GREEN,
        padding=10
    )

    side_bar = ft.Container(
        content=ft.Column(
            [
                ft.Text(value="Side Bar", style="titleLarge"),
                checkbox1,
                checkbox2,
                checkbox3
            ]
        ),
        width=200,
        bgcolor=ft.colors.AMBER,
        padding=10
    )


    graph_bar = ft.Container(
        content=ft.Text(
            value="Graph Bar",
            style="titleMedium"
        ),
        height=100,
        bgcolor=ft.colors.LIGHT_BLUE,
        padding=10
    )


    layout = ft.Column(
        [
            nav_bar,
            ft.Row(
                [
                    main,
                    side_bar
                ],
                expand=True
            ),
            graph_bar
        ],
        expand=True
    )

    page.add(layout)


ft.app(target=home_view)
