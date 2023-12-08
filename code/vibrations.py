import math
from settings import *
from matplotlib import pyplot as plt
from datetime import datetime


def damped_vibrations(start_x, t, k, m, b):
    return (
        start_x
        * math.exp((-b / 2 * m) * t)
        * math.cos(math.sqrt((k / m) - (b / (2 * m)) ** 2) * t)
    )


x = []
y = []
t = 0


for _ in range(0, 1000, 1):
    a = damped_vibrations(1, t, 4200, 1.5, 1)
    t += 0.01
    x.append(t)
    y.append(a)

time_form = "%d.%m.%Y"

# plt.rcParams["figure.figsize"] = [12.00, 3.50]
# plt.rcParams["figure.autolayout"] = True
# plt.figure(f"Wykres drgań {datetime.now().strftime(time_form)}")
# plt.title("Wykres drgań x(t)")
# plt.xlim(0, t)
# plt.xlabel("Czas t")
# plt.ylim(-1, 1)
# plt.ylabel("Odchylenie x")
# plt.grid()
# plt.plot(
#                 x,
#                 y,
#                 marker="o",
#                 markersize=1,
#                 markeredgecolor="red",
#                 markerfacecolor="green",
#             )
# plt.show()
