import numpy as np


class Simulation:
    def __init__(self):
        self.current_points = tuple()
        self.simulation_time = 10
        self.time_step = 0.002

    async def update_points(self, vibrations_type: str, parameters):
        self.current_points = tuple()
        match vibrations_type:
            case "damped_vibrations":
                self.current_points = tuple(
                    self.damped_vibrations(time, parameters)[0]
                    for time in np.arange(0, 10, self.time_step)
                )

            case "forced_damped_vibrations":
                self.current_points = tuple(
                    self.forced_vibrations(time, parameters)[0]
                    for time in np.arange(0, 10, self.time_step)
                )

            case "dynamic_vibration_absorber":
                self.current_points = tuple(
                    self.dynamic_vibration_absorber(time, parameters)[0]
                    for time in np.arange(0, 10, self.time_step)
                )

    def damped_vibrations(self, time, parameters):
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

    def damped_vibrations_max(k, m, n):
        w_0 = np.sqrt(k / m)
        b = n / (2 * m)
        bk = 2 * w_0 * m
        return [b, bk]

    def forced_vibrations(self, time, parameters):
        mass = parameters["mass"].get_value()
        spring_constant = parameters["spring"].get_value()
        damping_coefficient = parameters["damping_coefficient"].get_value()
        excitation = parameters["excitation"].get_value()
        initial_displacement = 0.5

        w = np.sqrt(spring_constant / mass)
        p = excitation
        h = damping_coefficient

        numerator = 1 + 4 * ((p**2) / (w**2)) * ((h**2) / (w**2))
        denominator = (1 - (p**2) / (w**2)) ** 2 + 4 * ((h**2) / (w**2)) * (
            (p**2) / (w**2)
        )
        amplitude = initial_displacement * np.sqrt(numerator / denominator)
        displacement = amplitude * np.sin(p * time)

        return displacement, p / w

    def dynamic_vibration_absorber(self, time, parameters):
        mass1 = parameters["mass1"].get_value()
        spring1 = parameters["spring1"].get_value()
        mass2 = parameters["mass2"].get_value()
        spring2 = parameters["spring2"].get_value()
        force = 50

        p = np.sqrt(spring1 / mass1)

        denominator = (
            mass1 * mass2 * p**4
            - (mass1 * spring2 + (spring1 + spring2) * mass2) * p**2
            + spring1 * spring2
        )
        b1 = ((spring2 - mass2 * p**2) / denominator) * force
        b2 = (spring2 / denominator) * force
        y1 = b1 * np.sin(p * time)
        y2 = b2 * np.sin(p * time)

        optimal_k2 = mass2 * p**2

        return y1, y2, optimal_k2


simulation = Simulation()
