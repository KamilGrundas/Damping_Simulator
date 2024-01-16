import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def model_objekt1(y, t):
    x, v = y
    dydt = [v, (30 * np.sin(t) - 1800 * x - 2 * v) / 50]
    return dydt


def model_objekt2(y, t):
    x, v = y
    dydt = [v, (-1800 * x - 0.1 * v) / 2]  # Poprawiony współczynnik tłumienia
    return dydt


# Warunki początkowe
y0 = [0, 0]

# Czasy, dla których będziemy rozwiązywać równanie
t = np.linspace(0, 10, 1000)

# Rozwiązanie równania różniczkowego dla objektu 1
sol_objekt1 = odeint(model_objekt1, y0, t)

# Rozwiązanie równania różniczkowego dla objektu 2
sol_objekt2 = odeint(model_objekt2, y0, t)

# Wykres poziomu odchylenia od czasu dla obiektu 1 (czerwony kolor) i obiektu 2 (zielony kolor)
plt.plot(t, sol_objekt1[:, 0], "r", label="Objekt 1")
plt.plot(t, sol_objekt2[:, 0], "g", label="Objekt 2")
plt.xlabel("Czas")
plt.ylabel("Odchylenie")
plt.legend()
plt.show()


omega_1 = (
    m_1 * k_2
    + (k_1 + k_2) * m_2
    - sqrt(
        m_1**2 * k_2**2 + (k_1 + k_2) ** 2 * m_2 + 2 * k_2 * m_1 * m_2 * (k_2 - k_1)
    )
) / (2 * m_1 * m_2)
omega_2 = (
    m_1 * k_2
    + (k_1 + k_2) * m_2
    + sqrt(
        m_1**2 * k_2**2 + (k_1 + k_2) ** 2 * m_2 + 2 * k_2 * m_1 * m_2 * (k_2 - k_1)
    )
) / (2 * m_1 * m_2)
