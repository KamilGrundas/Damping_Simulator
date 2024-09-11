import math
from settings import *
import numpy as np


def damped_vibrations(start_y, t, k, m, n):
    w_0 = np.sqrt(k / m)

    b = n / (2 * m)

    try:
        w = np.sqrt((w_0**2) - (b / (2 * m)) ** 2)
        w_t = np.sqrt(w**2 - b**2)
    except:
        w = 0
        w_t = np.sqrt(w**2 - b**2)
    if w_0 == 0:
        y = start_y
    else:
        y = start_y * np.exp((-b / (2 * m)) * t) * np.cos(w * t)

    return y, w, w_t


def damped_vibrations_max(k, m, n):
    w_0 = np.sqrt(k / m)
    b = n / (2 * m)
    bk = 2 * w_0 * m
    return [b, bk]


# def forced_vibrations(m, w, r, k, t):
#     b = 0.1
#     y = (
#         (m * (w**2) * r) / np.sqrt(((k - m * (w) ** 2) ** 2) + (b * w) ** 2)
#     ) * np.cos(w * t)
#     return y


def forced_vibrations(m, k, h, p, t):
    a = 0.5
    w = np.sqrt(k / m)
    y = a*  np.sqrt((1+4*((p**2)/(w**2))*((h**2)/(w**2)))/((1-((p**2)/(w**2)))**2 +4*(((h**2)/(w**2))*((p**2)/(w**2)))))*np.sin(p*t)
    #y = (a * np.sin(p*t)) / np.sqrt(((k - m * (w) ** 2) ** 2) + (h * w) ** 2)

    return y, p/w

def dynamic_dumping(m1,k1,m2, k2, t):

    force = 50

    p = np.sqrt(k1/m1)

    # Calculate B1 and B2 using the provided formulas
    denominator = m1 * m2 * p**4 - (m1 * k2 + (k1 + k2) * m2) * p**2 + k1 * k2
    b1 = (k2 - m2 * p**2) / denominator * force
    b2 = k2 / denominator * force
    y1 = b1 * np.sin(p * t)
    y2 = b2 * np.sin(p * t)

    optimal_k2 = m2 * p**2

    return y1, y2, optimal_k2
