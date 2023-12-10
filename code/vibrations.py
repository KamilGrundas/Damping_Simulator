import math
from settings import *


def damped_vibrations(start_y, t, k, m, n):
    w_0 = math.sqrt(k / m)
    h = math.sqrt((w_0**2) * ((n**2) / ((n**2) + math.pi**2)))
    b = 2 * h * m

    w = math.sqrt((w_0**2) - (b / (2 * m)) ** 2)
    y = start_y * math.exp((-b / (2 * m)) * t) * math.cos(w * t)
    return y


def damped_vibrations_max(k, m, n):
    w_0 = math.sqrt(k / m)
    h = math.sqrt((w_0**2) * ((n**2) / ((n**2) + math.pi**2)))
    b = 2 * h * m
    bk = 2 * w_0 * m
    return [b, bk]
