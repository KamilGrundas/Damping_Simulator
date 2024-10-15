import numpy as np


class Simulation:
    def __init__(self):
        self.current_points = []
        self.time_step = 0.01

    async def update_points(self, vibrations_type, parameters):
        self.current_points = []
        time = 0
        match vibrations_type:
            case "damped_vibrations":
                while time < 120:
                    self.current_points.append(
                        self.damped_vibrations(time, parameters)[0]
                    )
                    time += self.time_step

            case "forced_vibrations":
                pass

            case "dynamic_damping":
                pass

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

    def forced_vibrations(m, k, h, p, t):
        a = 0.5
        w = np.sqrt(k / m)
        y = (
            a
            * np.sqrt(
                (1 + 4 * ((p**2) / (w**2)) * ((h**2) / (w**2)))
                / (
                    (1 - ((p**2) / (w**2))) ** 2
                    + 4 * (((h**2) / (w**2)) * ((p**2) / (w**2)))
                )
            )
            * np.sin(p * t)
        )
        # y = (a * np.sin(p*t)) / np.sqrt(((k - m * (w) ** 2) ** 2) + (h * w) ** 2)

        return y, p / w

    def dynamic_dumping(m1, k1, m2, k2, t):

        force = 50

        p = np.sqrt(k1 / m1)

        denominator = m1 * m2 * p**4 - (m1 * k2 + (k1 + k2) * m2) * p**2 + k1 * k2
        b1 = (k2 - m2 * p**2) / denominator * force
        b2 = k2 / denominator * force
        y1 = b1 * np.sin(p * t)
        y2 = b2 * np.sin(p * t)

        optimal_k2 = m2 * p**2

        return y1, y2, optimal_k2


simulation = Simulation()
