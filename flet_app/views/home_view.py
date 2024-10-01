import flet as ft
from i18n.language import language
import asyncio

from flet_app.components.navigation_bar import NavigationBar
from flet_app.components.side_bar import SideBar
from flet_app.components.main_content import MainContent
from flet_app.components.graph_bar import GraphBar

from flet_app.classes.animation import DampedVibrationAnimator


def home_view(page: ft.Page):
    page.title = language.get("page_title")

    def change_language(e):
        selected_lang_code = navigation_bar.dropdown.value
        language.set_language(selected_lang_code)
        page.clean()
        home_view(page)

    rectangle = ft.Container(
        bgcolor=ft.colors.BLACK,
        width=200,
        height=100,
        top=20,
    )

    time_text = ft.Text(
        value="0.00",
        color=ft.colors.WHITE,
        size=16,
        left=10,
        top=10,
    )
    def animate_spring(e):
        if spring_image_container.height == 300:
            spring_image_container.height = 200
        else:
            spring_image_container.height = 300
        page.update()

    spring_image_container = ft.Container(
        content=ft.Image(
            src="/spring.png",
            width=100,
            height=300,
        ),
        width=100,
        height=300,
        animate=ft.animation.Animation(9500, ft.AnimationCurve.ELASTIC_OUT),
    )

    main_content = MainContent(rectangle,spring_image_container, time_text)
    graph_bar = GraphBar()
    navigation_bar = NavigationBar(on_language_change=change_language)
    side_bar = SideBar()

    layout = ft.Column(
        controls=[
            navigation_bar.view,
            ft.Row(
                controls=[
                    ft.Container(content=main_content.view, expand=True),
                    ft.Column(
                        controls=[
                            side_bar.view,
                            ft.ElevatedButton(
                                "Plot Graph",
                                on_click=lambda e: graph_bar.update_graph(
                                    side_bar.sliders_dict["damped_vibrations"]
                                ),
                            ),
                            ft.ElevatedButton(
                                "Reset",
                                on_click=lambda e: asyncio.run(animation.timer.reset()),
                            ),
                            ft.ElevatedButton("Animate Spring!", on_click=animate_spring),
                            ft.ElevatedButton(
                                "Start",
                                on_click=lambda e: asyncio.run(animation.timer.start()),
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.START,
                    ),
                ],
                expand=True,
                vertical_alignment=ft.CrossAxisAlignment.START,
            ),
            graph_bar.view,
        ],
        expand=True,
    )

    animation = DampedVibrationAnimator(rectangle, side_bar.sliders_dict, time_text)
    page.add(layout)
    page.scroll = True
