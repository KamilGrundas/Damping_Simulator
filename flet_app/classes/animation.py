from flet_app.classes.timer import Timer
import numpy as np


class DampedVibrationAnimator:
    def __init__(self, rectangle, sliders_dict, time_text):
        self.rectangle = rectangle
        self.sliders_dict = sliders_dict["damped_vibrations"]
        self.timer = Timer()
        self.time_text = time_text
        self.amplitude = 2

    def animate_rectangle(self, time):
        displacement = damped_vibrations(time, self.sliders_dict)[0]
        self.rectangle.left = 300 + displacement * 100
        self.rectangle.update()

        self.time_text.value = self.timer.get_formatted_time()
        self.time_text.update()

    async def start_animation(self):
        self.timer.on_change(self.animate_rectangle)
        await self.timer.start()


def damped_vibrations(time, parameters):
    spring_constant = parameters["spring_constant"].get_value()
    mass = parameters["mass"].get_value()
    damping_coefficient = parameters["damping_coefficient"].get_value()
    initial_displacement = 2

    natural_frequency = np.sqrt(spring_constant / mass)

    damping_factor = damping_coefficient / (2 * mass)

    try:
        damped_frequency = np.sqrt(
            (natural_frequency**2) - (damping_factor / (2 * mass)) ** 2
        )
        damped_frequency_with_correction = np.sqrt(
            damped_frequency**2 - damping_factor**2
        )
    except:
        damped_frequency = 0
        damped_frequency_with_correction = np.sqrt(
            damped_frequency**2 - damping_factor**2
        )

    if natural_frequency == 0:
        displacement = initial_displacement
    else:
        displacement = (
            initial_displacement
            * np.exp((-damping_factor / (2 * mass)) * time)
            * np.cos(damped_frequency * time)
        )

    return displacement, damped_frequency, damped_frequency_with_correction
