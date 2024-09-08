import flet as ft
from i18n.language import language
import asyncio
import numpy as np
import matplotlib.pyplot as plt
import io
from PIL import Image as PilImage
import base64



def damped_vibrations(start_y, t, k, m, n):
    w_0 = np.sqrt(k / m)

    b = n / (2 * m)

    try:
        w = np.sqrt((w_0**2) - (b / (2 * m)) ** 2)
        w_t = np.sqrt(w**2 - b**2)
    except:
        w = 0
        w_t = np.sqrt(w**2 - b**2)
    if w_0 == 0:
        y = start_y
    else:
        y = start_y * np.exp((-b / (2 * m)) * t) * np.cos(w * t)

    return y, w, w_t

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
        update_side_bar()
        page.update()

    def update_side_bar():
        # Show or hide sidebars based on checkbox values
        side_bar_main_content1.visible = checkbox1.value
        side_bar_main_content2.visible = checkbox2.value
        side_bar_main_content3.visible = checkbox3.value
        page.update()

    def on_slider_change(slider, text_field):
        text_field.value = str(round(slider.value, 2))
        time_text.value = "0.00"
        page.update()

    def on_text_change(text_field, slider):
        try:
            value = float(text_field.value)
            slider.value = value
            time_text.value = "0.00"
            page.update()
        except ValueError:
            pass


    
    def update_graph():
        # Generate a plot using Matplotlib
        fig, ax = plt.subplots()
        time = np.linspace(0, 10, 1000)
        start_y = 1
        k = slider_spring1.value
        m = slider_mass1.value
        n = slider_damping1.value

        y_values = [damped_vibrations(start_y, t, k, m, n)[0] for t in time]
        ax.plot(time, y_values)

        # Save the plot to a BytesIO buffer
        buf = io.BytesIO()
        plt.savefig(buf, format="png")
        buf.seek(0)

        # Convert the image to base64
        pil_image = PilImage.open(buf)
        img_byte_arr = io.BytesIO()
        pil_image.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()

        # Encode as base64
        img_base64 = base64.b64encode(img_byte_arr).decode('utf-8')

        # Create the Flet image component from the base64 string
        flet_image = ft.Image(src_base64=img_base64, width=1000, height=100)

        # Add the image to the page
        graph_bar.content = flet_image
        page.update()


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
        on_change=lambda e: update_checkbox(checkbox1, [checkbox1, checkbox2, checkbox3]),
    )
    checkbox2 = ft.Checkbox(
        label=language.get("forced_damped_vibrations"),
        value=False,
        on_change=lambda e: update_checkbox(checkbox2, [checkbox1, checkbox2, checkbox3]),
    )
    checkbox3 = ft.Checkbox(
        label=language.get("dynamic_vibration_absorber"),
        value=False,
        on_change=lambda e: update_checkbox(checkbox3, [checkbox1, checkbox2, checkbox3]),
    )

    # Sliders and TextFields for checkbox1
    slider_damping1 = ft.Slider(min=0, max=10, value=5, on_change=lambda e: on_slider_change(slider_damping1, text_damping1))
    text_damping1 = ft.TextField(width=90, value="5", on_change=lambda e: on_text_change(text_damping1, slider_damping1))

    slider_spring1 = ft.Slider(min=0, max=5000, value=2500, on_change=lambda e: on_slider_change(slider_spring1, text_spring1))
    text_spring1 = ft.TextField(width=90, value="2500", on_change=lambda e: on_text_change(text_spring1, slider_spring1))

    slider_mass1 = ft.Slider(min=0.1, max=2, value=1.05, on_change=lambda e: on_slider_change(slider_mass1, text_mass1))
    text_mass1 = ft.TextField(width=90, value="1.05", on_change=lambda e: on_text_change(text_mass1, slider_mass1))

    # Sliders and TextFields for checkbox2
    slider_damping2 = ft.Slider(min=0, max=20, value=10, on_change=lambda e: on_slider_change(slider_damping2, text_damping2))
    text_damping2 = ft.TextField(width=90, value="10", on_change=lambda e: on_text_change(text_damping2, slider_damping2))

    slider_excitation2 = ft.Slider(min=0, max=50, value=25, on_change=lambda e: on_slider_change(slider_excitation2, text_excitation2))
    text_excitation2 = ft.TextField(width=90, value="25", on_change=lambda e: on_text_change(text_excitation2, slider_excitation2))

    slider_spring2 = ft.Slider(min=75, max=200, value=137.5, on_change=lambda e: on_slider_change(slider_spring2, text_spring2))
    text_spring2 = ft.TextField(width=90, value="137.5", on_change=lambda e: on_text_change(text_spring2, slider_spring2))

    slider_mass2 = ft.Slider(min=1, max=5, value=3, on_change=lambda e: on_slider_change(slider_mass2, text_mass2))
    text_mass2 = ft.TextField(width=90, value="3", on_change=lambda e: on_text_change(text_mass2, slider_mass2))

    # Sliders and TextFields for checkbox3
    slider_mass1_3 = ft.Slider(min=45, max=100, value=72.5, on_change=lambda e: on_slider_change(slider_mass1_3, text_mass1_3))
    text_mass1_3 = ft.TextField(width=90, value="72.5", on_change=lambda e: on_text_change(text_mass1_3, slider_mass1_3))

    slider_spring1_3 = ft.Slider(min=500, max=2500, value=1500, on_change=lambda e: on_slider_change(slider_spring1_3, text_spring1_3))
    text_spring1_3 = ft.TextField(width=90, value="1500", on_change=lambda e: on_text_change(text_spring1_3, slider_spring1_3))

    slider_mass2_3 = ft.Slider(min=0.5, max=4.5, value=2.5, on_change=lambda e: on_slider_change(slider_mass2_3, text_mass2_3))
    text_mass2_3 = ft.TextField(width=90, value="2.5", on_change=lambda e: on_text_change(text_mass2_3, slider_mass2_3))

    slider_spring2_3 = ft.Slider(min=25, max=225, value=125, on_change=lambda e: on_slider_change(slider_spring2_3, text_spring2_3))
    text_spring2_3 = ft.TextField(width=90, value="125", on_change=lambda e: on_text_change(text_spring2_3, slider_spring2_3))


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

    side_bar_main_content1 = ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Text(value="Damping", width=100),
                        text_damping1,
                        slider_damping1
                    ],
                    alignment="end",
                    width=500
                ),
                ft.Row(
                    controls=[
                        ft.Text(value="Spring Stiffness", width=100),
                        text_spring1,
                        slider_spring1
                    ],
                    alignment="end",
                    width=500
                ),
                ft.Row(
                    controls=[
                        ft.Text(value="Mass", width=100),
                        text_mass1,
                        slider_mass1
                    ],
                    alignment="end",
                    width=500
                ),
            ]
        ),
        width=400,
        bgcolor=ft.colors.AMBER,
        padding=10,
        visible=True  # Initially visible
    )

    side_bar_main_content2 = ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Text(value="Damping", width=100),
                        text_damping2,
                        slider_damping2
                    ],
                    alignment="end",
                    width=500
                ),
                ft.Row(
                    controls=[
                        ft.Text(value="Excitation Frequency", width=100),
                        text_excitation2,
                        slider_excitation2
                    ],
                    alignment="end",
                    width=500
                ),
                ft.Row(
                    controls=[
                        ft.Text(value="Spring Stiffness", width=100),
                        text_spring2,
                        slider_spring2
                    ],
                    alignment="end",
                    width=500
                ),
                ft.Row(
                    controls=[
                        ft.Text(value="Mass", width=100),
                        text_mass2,
                        slider_mass2
                    ],
                    alignment="end",
                    width=500
                ),
            ]
        ),
        width=400,
        bgcolor=ft.colors.AMBER,
        padding=10,
        visible=False
    )

    side_bar_main_content3 = ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Text(value="Mass 1", width=100),
                        text_mass1_3,
                        slider_mass1_3
                    ],
                    alignment="end",
                    width=500
                ),
                ft.Row(
                    controls=[
                        ft.Text(value="Spring 1", width=100),
                        text_spring1_3,
                        slider_spring1_3
                    ],
                    alignment="end",
                    width=500
                ),
                ft.Row(
                    controls=[
                        ft.Text(value="Mass 2", width=100),
                        text_mass2_3,
                        slider_mass2_3
                    ],
                    alignment="end",
                    width=500
                ),
                ft.Row(
                    controls=[
                        ft.Text(value="Spring 2", width=100),
                        text_spring2_3,
                        slider_spring2_3
                    ],
                    alignment="end",
                    width=500
                ),
            ]
        ),
        width=400,
        bgcolor=ft.colors.AMBER,
        padding=10,
        visible=False
    )

    # Set initial visibility for the content sections
    update_side_bar()


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

    async def animate_rectangle(rectangle):
        amplitude = 2
        

        while True:
            time = float(time_text.value)
            time += 0.01
            rectangle.left = 300 + damped_vibrations(amplitude, time, slider_spring1.value, slider_mass1.value, slider_damping1.value)[0]*100
            rectangle.update()
            time_text.value = str(round(time,2))
            time_text.update()
            await asyncio.sleep(0.01)

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
        right=10,
        bottom=10,
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

    # Navigation bar and sidebar
    dropdown = ft.Dropdown(
        label="Language",
        options=[
            ft.dropdown.Option(key="en", text="English"),
            ft.dropdown.Option(key="pl", text="Polski")
        ],
        value="en",
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
                            side_bar_main_content1,
                            side_bar_main_content2,
                            side_bar_main_content3
                        ]
                    )
                ],
                expand=True
            )
        ],
        expand=True
    )

    page.add(layout)
    update_side_bar()
    # Start the animation
    page.add(ft.ElevatedButton("Start Animation", on_click=lambda e: asyncio.run(animate_rectangle(rectangle))))
    page.add(ft.ElevatedButton("Plot Graph", on_click=lambda e: update_graph()))

ft.app(target=home_view)
