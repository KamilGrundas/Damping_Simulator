import math
from settings import *
import numpy as np


def damped_vibrations(start_y, t, k, m, n):
    w_0 = np.sqrt(k / m)

    b = n / (2 * m)

    try:
        w = np.sqrt((w_0**2) - (b / (2 * m)) ** 2)
    except:
        w = 0
    if w_0 == 0:
        y = start_y
    else:
        y = start_y * np.exp((-b / (2 * m)) * t) * np.cos(w * t)

    return y


def damped_vibrations_max(k, m, n):
    w_0 = np.sqrt(k / m)
    b = n / (2 * m)
    bk = 2 * w_0 * m
    return [b, bk]


def forced_vibrations(m, w, r, k, t):
    b = 0.1
    y = (
        (m * (w**2) * r) / np.sqrt(((k - m * (w) ** 2) ** 2) + ((b * (w**2)) ** 2))
    ) * np.cos(w * t)
    return y


def dynamic_dumping(m2, k2, t):
    k1 = 1800
    m1 = 50
    f = 50
    p0 = 2 * np.pi
    p = p0

    # Calculate B1 and B2 using the provided formulas
    denominator = m1 * m2 * p**4 - (m1 * k2 + (k1 + k2) * m2) * p**2 + k1 * k2
    b1 = (k2 - m2 * p**2) / denominator * f
    b2 = k2 / denominator * f
    y1 = b1 * np.sin(p * t)
    y2 = b2 * np.sin(p * t)

    return y1, y2
