import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


class Solution():
    def __init__(self):
        self.solution = []
        # Parametry układu
        self.m1 = 50  # masa objektu 1 [kg]
        self.k1 = 1800  # stała sprężystości sprężyny 1 [N/m]
        self.k2 = 100  # stała sprężystości sprężyny 2 (tłumika) [N/m]
        self.m2 = 2  # masa objektu 2 [kg]
        self.F1_amplitude = 30  # amplituda siły F1 [N]
        self.DUMP = True  # czy uwzględniamy objekt 2 (tłumik) czy nie
    
    # Funkcja opisująca układ równań różniczkowych
    def model(self,y, t):
        x1, v1, x2, v2 = y

        # Równania ruchu dla obiektu 1
        dx1dt = v1
        dv1dt = (self.F1_amplitude * np.sin(t) - self.k1 * x1 - (self.k2 * (x1 - x2) if self.DUMP else 0)) / self.m1

        # Równania ruchu dla obiektu 2 (tłumik drgań)
        dx2dt = v2
        dv2dt = (self.k2 * (x1 - x2) - self.k2 * x2) / self.m2 if self.DUMP else 0

        return [dx1dt, dv1dt, dx2dt, dv2dt]
    
    def generate_solution(self):
        # Warunki początkowe
        y0 = [0, 0, 0, 0]

        # Czas symulacji
        t = np.linspace(0, 100, 100000)
        # Rozwiązanie układu równań różniczkowych
        solution = odeint(self.model, y0, t)

        # Indeks odpowiadający czasowi t = 0.06
        index_for_t_06 = np.argmax(t >= 40)

        # Odczytanie odchylenia dla t = 0.06 dla obiektu 1 i obiektu 2
        odchylenie_objekt1_t_06 = solution[index_for_t_06, 0]
        odchylenie_objekt2_t_06 = solution[index_for_t_06, 2]

        print(f"Odchylenie dla t = 0.06 dla objektu 1: {odchylenie_objekt1_t_06}")
        print(f"Odchylenie dla t = 0.06 dla objektu 2: {odchylenie_objekt2_t_06}")



# Wykresy
# plt.plot(t, solution[:, 0], label='Objekt 1')
# if DUMP:
#     plt.plot(t, solution[:, 2], label='Objekt 2 (tłumik)')
# plt.xlabel('Czas [s]')
# plt.ylabel('Odchylenie od stanu równowagi [m]')
# plt.legend()
# plt.grid(True)
# plt.show()

