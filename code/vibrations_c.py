import math
from settings import *


def damped_vibrations(start_y, t, k, m, n):
    w_0 = math.sqrt(k / m)
    b = n / (2 * m)

    delta = 4 * (b**2) - 4 * (w_0**2)

    if delta < 0:
        w = math.sqrt((w_0**2) - (b**2))
        y = start_y * math.exp(-b * t) * math.cos(w * t)
    elif delta > 0:
        a_1 = -b - math.sqrt(b**2 - w_0**2)
        a_2 = -b + math.sqrt(b**2 - w_0**2)
        y = start_y * math.exp(a_1 * t) + start_y * math.exp(a_2 * t)

    else:
        y = 0
        print("ERROR")
    return y


def damped_vibrations_max(k, m, n):
    w_0 = math.sqrt(k / m)
    b = n / (2 * m)
    delta = 4 * (b**2) - 4 * (w_0**2)
    bk = b
    return [b, bk]
