import flet as ft
from i18n.language import language
import asyncio
import numpy as np
import matplotlib.pyplot as plt
import io
from PIL import Image as PilImage
import base64
from flet.matplotlib_chart import MatplotlibChart
from flet_app.classes.timer import Timer
from flet_app.classes.input_slider import SliderWithText
from flet_app.classes.animation import DampedVibrationAnimator, damped_vibrations
import json


with open("flet_app/views/widgets_config.json") as f:
    config = json.load(f)

import numpy as np




def home_view(page: ft.Page):


    def change_language(e):
        selected_lang_code = dropdown.value
        language.set_language(selected_lang_code)
        page.clean()
        home_view(page)

    def update_checkbox(selected, checkboxes, controls):
        for checkbox in checkboxes:
            if checkbox != selected:
                checkbox.value = False
        side_bar_main.content.controls = controls
        page.update()



    
    def update_graph():
        # Generate a plot using Matplotlib
        fig, ax = plt.subplots()
        time = np.linspace(0, 10, 10000)
        parameters = sliders_dict["damped_vibrations"]

        y_values = [damped_vibrations(t, parameters)[0] for t in time]
        ax.plot(time, y_values)

        # Set axis labels and legend
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Amplitude")
        ax.legend(title="Damped Vibrations")

        # Update the graph bar with the new chart
        graph_bar.content = MatplotlibChart(fig, expand=True)
        graph_bar.update()


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

    checkbox1 = ft.Checkbox(
        label=language.get("damped_vibrations"),
        value=True,
        on_change=lambda e: update_checkbox(checkbox1, [checkbox1, checkbox2, checkbox3], sliders[0:4]),
    )
    checkbox2 = ft.Checkbox(
        label=language.get("forced_damped_vibrations"),
        value=False,
        on_change=lambda e: update_checkbox(checkbox2, [checkbox1, checkbox2, checkbox3], sliders[4:9]),
    )
    checkbox3 = ft.Checkbox(
        label=language.get("dynamic_vibration_absorber"),
        value=False,
        on_change=lambda e: update_checkbox(checkbox3, [checkbox1, checkbox2, checkbox3], sliders[9:]),
    )

    sliders_dict = {}

    def create_sliders_from_json(data):
        rows = []

        # Iterate over each level in the JSON data
        for level_name, controls in data.items():
            rows.append(ft.Text(value=level_name, style="titleMedium"))  # Section title

            sliders_dict[level_name] = {}

            # Iterate over the individual control elements
            for control_name, control_data in controls.items():
                min_val = control_data["min"]
                max_val = control_data["max"]
                default_val = control_data["default_value"]

                slider_with_text = SliderWithText(
                    min_val, max_val, default_val, control_name
                )
                sliders_dict[level_name][control_name] = slider_with_text
                row = slider_with_text.create_row()
                rows.append(row)  # Add the row to the list

        return rows

    sliders = create_sliders_from_json(config)



    side_bar_top = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text(value="Side Bar", style="titleLarge"),
                checkbox1,
                checkbox2,
                checkbox3,
            ]
        ),
        width=400,
        bgcolor=ft.colors.AMBER,
        padding=10
    )

    side_bar_main = ft.Container(
        content=ft.Column(
            controls=sliders[0:4]
        ),
        width=400,
        bgcolor=ft.colors.AMBER,
        padding=10,
        visible=True  # Initially visible
    )


    nav_bar = ft.Container(
        content=ft.Row(
            controls=[
                ft.Text(
                    value="Navigation Bar",
                    style="headlineSmall",
                ),
                dropdown,
            ],
            alignment="spaceBetween",
        ),
        height=100,
        bgcolor=ft.colors.BLUE,
        padding=10,
    )



    rectangle = ft.Container(
        bgcolor=ft.colors.BLACK,
        width=100,
        height=100,
        left=(1000 - 100) // 2,
        top=20,
    )
    # Tworzenie licznika czasu
    time_text = ft.Text(
        value="0.00",
        color=ft.colors.WHITE,
        size=16,
        # Pozycjonowanie w prawym dolnym rogu kontenera
        left=10,
        top=10,
    )

    # Main content
    main = ft.Container(
        content=ft.Stack(
            controls=[rectangle, time_text],
            width=1000,
            height=500
        ),
        expand=True,
        height=900,
        bgcolor=ft.colors.LIGHT_GREEN,
        padding=10
    )


    side_bar_top = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text(value="Side Bar", style="titleLarge"),
                checkbox1,
                checkbox2,
                checkbox3,
            ]
        ),
        width=400,
        bgcolor=ft.colors.AMBER,
        padding=10
    )

    nav_bar = ft.Container(
        content=ft.Row(
            controls=[
                ft.Text(value="Navigation Bar", style="headlineSmall"),
                dropdown,
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        height=100,
        bgcolor=ft.colors.BLUE,
        padding=10,
    )

    # Graph bar
    graph_bar = ft.Container(
        content=ft.Text(
            value="Graph Bar",
            style="titleMedium"
        ),
        height=700,
        bgcolor=ft.colors.LIGHT_BLUE,
        padding=10
    )

    # Layout
    layout = ft.Column(
        controls=[
            nav_bar,
            ft.Row(
                controls=[
                    ft.Column(
                        controls = [main, graph_bar]
                    ),
                    ft.Column(
                        controls=[
                            side_bar_top,
                            side_bar_main
                        ]
                    )
                ],
                expand=True
            )
        ],
        expand=True
    )
    
    animation = DampedVibrationAnimator(rectangle,sliders_dict,time_text)
    page.add(layout)

    page.add(ft.ElevatedButton("Start Animation", on_click=lambda e: asyncio.run(animation.start_animation())))
    page.add(ft.ElevatedButton("Plot Graph", on_click=lambda e: update_graph()))

