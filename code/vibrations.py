import math
from matplotlib import pyplot as plt
from datetime import datetime

def w(k,m, b):
    return math.sqrt((k/m)-(b/(2*m))**2)

x = []
y = []
t = 0
odchyl = 1

for _ in range(0,1000,1):
    a = odchyl*math.exp((-1.5/2)*t)*math.cos(w(600,1,1.5)*t)
    x.append(t)
    y.append(a)
    t += 0.01

plt.rcParams["figure.figsize"] = [12.00, 3.50]
plt.rcParams["figure.autolayout"] = True
plt.figure(f"Wykres drgań {datetime.now().strftime("%d.%m.%Y")}")
plt.title("Wykres drgań x(t)")
plt.xlim(0, t)
plt.xlabel("Czas t")
plt.ylim(-odchyl, odchyl)
plt.ylabel("Odchylenie x")
plt.grid()
plt.plot(
                x,
                y,
                marker="o",
                markersize=1,
                markeredgecolor="red",
                markerfacecolor="green",
            )
plt.show()
