import flet as ft  # Assuming ft is the library you're using
from i18n.language import language

class SliderWithText:

    def __init__(self, min_val, max_val, default_val, label):
        self.min_val = min_val
        self.max_val = max_val
        self.default_val = default_val
        self.label = label

        # Create a slider
        self.slider = ft.Slider(
            min=self.min_val, max=self.max_val, value=self.default_val
        )

        # Create a text field with initial value as slider's value
        self.text_field = ft.TextField(value=str(self.default_val), width=75, text_size=14)

        # Bind event handlers
        self.slider.on_change = self.on_slider_change
        self.text_field.on_change = self.on_text_change

    def on_slider_change(self, e):
        self.text_field.value = str(
            round(self.slider.value, 2)
        )

        # Sync slider value with text field
        self.text_field.update()

    def on_text_change(self, e):
        try:
            # Ensure the input is valid before updating the slider
            new_value = float(self.text_field.value)
            if self.min_val <= new_value <= self.max_val:
                self.slider.value = new_value  # Sync text field value with slider
                self.slider.update()
        except ValueError:
            pass  # Ignore if the input is not a valid float

    def update_graph(self):
        # Placeholder for the update graph logic
        pass

    def create_row(self):
        # Return a row with a label, slider, and text field
        return ft.Row(
            controls=[
                ft.Text(value=language.get(self.label), width=90,size=12),
                self.slider,
                self.text_field,
            ]
        )

    def get_value(self):
        # Return the current value of the slider
        return self.slider.value