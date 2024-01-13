import numpy as np
import matplotlib.pyplot as plt

# Parametry układu
m1 = 50  # masa objektu 1 [kg]
k1 = 1200  # stała sprężystości sprężyny 1 [N/m]

# Nowe parametry tłumika (objektu 2)
m2 = 10  # masa objektu 2 [kg]
k2 = 100  # stała sprężystości sprężyny 2 (tłumika) [N/m]
c2 = 50  # tłumienie [Ns/m]

F1_amplitude = 30  # amplituda siły F1 [N]
DAMPING = True  # czy uwzględniamy objekt 2 (tłumik) czy nie

# Funkcja opisująca układ równań różniczkowych
def model(t, y):
    x1, v1, x2, v2 = y

    # Równania ruchu dla obiektu 1
    dx1dt = v1
    dv1dt = (F1_amplitude * np.sin(t) - k1 * x1 - (c2 * (v1 - v2) + k2 * (x1 - x2) if DAMPING else 0)) / m1

    # Równania ruchu dla obiektu 2 (tłumik drgań)
    dx2dt = v2
    dv2dt = (c2 * (v1 - v2) + k2 * (x1 - x2)) / m2 if DAMPING else 0

    return np.array([dx1dt, dv1dt, dx2dt, dv2dt])

# Warunki początkowe
y0 = np.array([0, 0, 0, 0])

# Czas symulacji
t_max = 10
dt = 0.01
t = np.arange(0, t_max, dt)

# Numeryczne rozwiązanie układu równań różniczkowych za pomocą metody Eulera
solution = np.zeros((len(t), len(y0)))
solution[0] = y0

for i in range(1, len(t)):
    y0 = y0 + dt * model(t[i-1], y0)
    solution[i] = y0

# Wykresy
plt.plot(t, solution[:, 0], label='Objekt 1')
if DAMPING:
    plt.plot(t, solution[:, 2], label='Objekt 2 (tłumik)')
plt.xlabel('Czas [s]')
plt.ylabel('Odchylenie od stanu równowagi [m]')
plt.legend()
plt.grid(True)
plt.show()
