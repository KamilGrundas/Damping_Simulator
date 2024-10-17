from flet_app.classes.simulation import simulation
from typing import Optional
import asyncio
import flet as ft
import time


class Animator:
    BASE_WIDTH = 50
    MIN_HEIGHT = 250
    MAX_HEIGHT = 400

    BASE_WIDTH_2 = 25
    MIN_HEIGHT_2 = 50
    MAX_HEIGHT_2 = 120

    def __init__(self):
        self.rectangle = ft.Container(
            bgcolor=ft.colors.BLACK,
            width=200,
            height=100,
            top=300,
        )

        self.spring = ft.Container(
            content=ft.Image(src="/spring.png", fit=ft.ImageFit.FILL),
            width=100,
            height=300,
        )

        self.time_text = ft.Text(
            value="0.0",
            color=ft.colors.BLACK87,
            size=16,
            left=10,
            top=10,
        )

        self.spring2 = ft.Container(
            content=ft.Image(src="/spring.png", fit=ft.ImageFit.FILL),
            width=50,
            top=400,
            height=150,
            visible=False,
        )

        self.rectangle2 = ft.Container(
            bgcolor=ft.colors.BLACK, width=50, height=50, top=550, visible=False
        )

        self.amplitude = 2
        self.time: Optional[float] = 0
        self.running = False

    def get_time(self) -> float:
        if self.time is not None:
            return round(self.time, 3)
        return 0.0

    def get_formatted_time(self) -> str:
        return "{:.1f}".format(self.time)

    def update_displacement(self, time_int):
        displacement = simulation.current_points[time_int]
        self.spring.height = 305 + displacement * 100

        current_height = max(min(self.spring.height, self.MAX_HEIGHT), self.MIN_HEIGHT)
        self.spring.width = self.BASE_WIDTH * (self.MAX_HEIGHT / current_height)
        self.spring.update()

        self.rectangle.top = 300 + displacement * 100
        self.rectangle.update()

    def update_dynamic_absorber(self, time_int):
        displacement = simulation.current_points_dynamic_absorber[time_int]
        self.spring2.height = 100 + displacement * 100

        current_height = max(
            min(self.spring2.height, self.MAX_HEIGHT_2), self.MIN_HEIGHT_2
        )
        self.spring2.width = self.BASE_WIDTH_2 * (self.MAX_HEIGHT_2 / current_height)
        self.spring2.top = 200 + self.rectangle.top - self.rectangle.height
        self.spring2.update()

        self.rectangle2.top = (
            100 + self.rectangle.top + self.rectangle.height + displacement * 100
        )
        self.rectangle2.update()

    def update_time_text(self):
        self.time_text.value = self.get_formatted_time()
        self.time_text.update()

    async def start(self, vibration_type):

        if self.running:
            return
        self.running = True
        i = 0
        start_time = time.time()
        while self.running:
            await asyncio.sleep(0.002)
            current_time = time.time()
            self.time += current_time - start_time
            start_time = current_time
            i += 1
            time_int = int(self.get_time() * 500)
            if time_int >= len(simulation.current_points):
                self.running = False
                break
            self.update_displacement(time_int)
            if vibration_type == "dynamic_vibration_absorber":
                self.update_dynamic_absorber(time_int)
            if i == 20:
                i = 0
                self.update_time_text()

    async def reset(self):
        self.running = False
        self.time = 0
        self.update_time_text()


animator = Animator()
