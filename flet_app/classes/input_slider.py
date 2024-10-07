import flet as ft
from i18n.language import language


class SliderWithText:
    def __init__(self, min_val, max_val, default_val, label, on_slider_change_callback=None):
        self.min_val = min_val
        self.max_val = max_val
        self.default_val = default_val
        self.label = label
        self.on_slider_change_callback = on_slider_change_callback

        self.slider = ft.Slider(
            min=self.min_val, max=self.max_val, value=self.default_val
        )

        self.text_field = ft.TextField(
            value=str(self.default_val), width=75, text_size=14
        )

        self.slider.on_change = self.combined_slider_change
        self.text_field.on_change = self.combined_text_change

    async def combined_slider_change(self, e):
        self.on_slider_change(e)
        if self.on_slider_change_callback:
            await self.on_slider_change_callback(e)

    async def combined_text_change(self, e):
        self.on_text_change(e)
        if self.on_slider_change_callback:
            await self.on_slider_change_callback(e)

    def on_slider_change(self, e):
        self.text_field.value = str(round(self.slider.value, 2))
        self.text_field.update()

    def on_text_change(self, e):
        try:
            new_value = float(self.text_field.value)
            if self.min_val <= new_value <= self.max_val:
                self.slider.value = new_value
                self.slider.update()
        except ValueError:
            pass

    def update_graph(self):
        pass

    def create_row(self):
        return ft.Row(
            controls=[
                ft.Text(value=language.get(self.label), width=90, size=12),
                self.slider,
                self.text_field,
            ]
        )

    def get_value(self):
        return self.slider.value