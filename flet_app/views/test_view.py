import flet as ft
from i18n.language import language
import asyncio
import numpy as np
import matplotlib.pyplot as plt
import io
from PIL import Image as PilImage
import base64
from flet_app.classes.timer import Timer
import json

with open("flet_app/views/widgets_config.json") as f:
    config = json.load(f)

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

    timer = Timer()

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



    
    def update_graph():
        # Generate a plot using Matplotlib
        fig, ax = plt.subplots()
        time = np.linspace(0, 10, 10000)
        start_y = 1
        k = sliders[2].controls[1].value
        m = sliders[3].controls[1].value
        n = sliders[1].controls[1].value

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

    def create_slider_and_text(min_val, max_val, default_val, label):
        # Create a slider
        slider = ft.Slider(min=min_val, max=max_val, value=default_val)

        # Create a text field with initial value as slider's value
        text_field = ft.TextField(value=str(default_val), width=90)

        # Function to update the text field when the slider value changes
        def on_slider_change(e):
            text_field.value = str(round(slider.value, 2))  # Sync slider value with text field
            timer.value = 0
            update_graph()
            text_field.update()

        # Function to update the slider when the text field value changes
        def on_text_change(e):
            try:
                # Ensure the input is valid before updating the slider
                new_value = float(text_field.value)
                if min_val <= new_value <= max_val:
                    slider.value = new_value  # Sync text field value with slider
                    timer.value = 0
                    update_graph()
                    slider.update()
            except ValueError:
                pass  # Ignore if the input is not a valid float

        # Bind event handlers for both slider and text field
        slider.on_change = on_slider_change
        text_field.on_change = on_text_change

        # Return a row with a label, slider, and text field
        return ft.Row(controls=[ft.Text(value=label, width=100), slider, text_field])

    def create_sliders_from_json(data):
        rows = []
        
        # Iterate over each level in the JSON data
        for level_name, controls in data.items():
            rows.append(ft.Text(value=level_name, style="titleMedium"))  # Section title
            
            # Iterate over the individual control elements
            for control_name, control_data in controls.items():
                min_val = control_data["min"]
                max_val = control_data["max"]
                default_val = control_data["default_value"]
                
                # Create slider and text field for each control
                row = create_slider_and_text(min_val, max_val, default_val, control_name)
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

    side_bar_main_content1 = ft.Container(
        content=ft.Column(
            controls=sliders[0:4]
        ),
        width=400,
        bgcolor=ft.colors.AMBER,
        padding=10,
        visible=True  # Initially visible
    )

    side_bar_main_content2 = ft.Container(
        content=ft.Column(
            controls=sliders[4:9]
        ),
        width=400,
        bgcolor=ft.colors.AMBER,
        padding=10,
        visible=False
    )

    side_bar_main_content3 = ft.Container(
        content=ft.Column(
            controls=sliders[9:]
        ),
        width=400,
        bgcolor=ft.colors.AMBER,
        padding=10,
        visible=False
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

    async def animate_rectangle(rectangle):
        amplitude = 2
        

        while True:
            timer.value += 0.01
            rectangle.left = 300 + damped_vibrations(amplitude, timer.value, sliders[2].controls[1].value, sliders[3].controls[1].value, sliders[1].controls[1].value)[0]*100
            rectangle.update()
            time_text.value = timer.get_formatted_time()
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

