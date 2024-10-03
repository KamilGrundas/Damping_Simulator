from flet_app.classes.timer import Timer
import numpy as np


class DampedVibrationAnimator:
    def __init__(self, rectangle, sliders_dict, time_text, spring, graph):
        self.rectangle = rectangle
        self.spring = spring
        self.sliders_dict = sliders_dict["damped_vibrations"]
        self.timer = Timer(graph, self.sliders_dict)
        self.time_text = time_text
        self.amplitude = 2
        self.timer.on_change(self.animate_rectangle)

    def animate_rectangle(self, time):

        displacement = damped_vibrations(time, self.sliders_dict)[0]

        self.spring.height = 305 + displacement * 100
        self.spring.update()

        base_width = 50
        min_height = 250
        max_height = 400

        current_height = max(min(self.spring.height, max_height), min_height)

        self.spring.width = base_width * (max_height / current_height)
        self.spring.update()

        self.rectangle.top = 300 + displacement * 100
        self.rectangle.update()

        self.time_text.value = self.timer.get_formatted_time()
        self.time_text.update()


def damped_vibrations(time, parameters):
    spring_constant = parameters["spring_constant"].get_value()
    mass = parameters["mass"].get_value()
    damping_coefficient = parameters["damping_coefficient"].get_value()
    initial_displacement = 3

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
