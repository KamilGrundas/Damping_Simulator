import math
from settings import *


def damped_vibrations(start_y, t, k, m, n):
    w_0 = math.sqrt(k / m)
    h = math.sqrt((w_0**2) * ((n**2) / ((n**2) + math.pi**2)))
    b = 2 * h * m
    bk = 2 * w_0 * m

    if t == 0:
        return start_y
    else:
        w = math.sqrt((w_0**2) - (b / (2 * m)) ** 2)
        y = start_y * math.exp((-b / 2 * m) * t) * math.cos(w * t)
        return y


# for _ in range(0, 1000, 1):
#     a = damped_vibrations(1, t, 4200, 1.5, 1)
#     t += 0.01
#     x.append(t)
#     y.append(a)
