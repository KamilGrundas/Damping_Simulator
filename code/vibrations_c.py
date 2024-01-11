import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Parametry układu
m1 = 50  # masa objektu 1 [kg]
k1 = 1800  # stała sprężystości sprężyny 1 [N/m]
k2 = 100  # stała sprężystości sprężyny 2 (tłumika) [N/m]
m2 = 2  # masa objektu 2 [kg]
F1_amplitude = 30  # amplituda siły F1 [N]
DUMP = True  # czy uwzględniamy objekt 2 (tłumik) czy nie

# Funkcja opisująca układ równań różniczkowych
def model(y, t):
    x1, v1, x2, v2 = y

    # Równania ruchu dla obiektu 1
    dx1dt = v1
    dv1dt = (F1_amplitude * np.sin(t) - k1 * x1 - (k2 * (x1 - x2) if DUMP else 0)) / m1

    # Równania ruchu dla obiektu 2 (tłumik drgań)
    dx2dt = v2
    dv2dt = (k2 * (x1 - x2) - k2 * x2) / m2 if DUMP else 0

    return [dx1dt, dv1dt, dx2dt, dv2dt]

# Warunki początkowe
y0 = [0, 0, 0, 0]

# Czas symulacji
t = np.linspace(0, 10, 1000)

# Rozwiązanie układu równań różniczkowych
solution = odeint(model, y0, t)

# Wykresy
plt.plot(t, solution[:, 0], label='Objekt 1')
if DUMP:
    plt.plot(t, solution[:, 2], label='Objekt 2 (tłumik)')
plt.xlabel('Czas [s]')
plt.ylabel('Odchylenie od stanu równowagi [m]')
plt.legend()
plt.grid(True)
plt.show()

