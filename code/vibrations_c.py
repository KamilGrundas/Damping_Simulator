import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

class Solution():
    def __init__(self):
        self.solution = []
        # Parametry układu
        self.m1 = 430  # masa objektu 1 [kg]
        self.k1 = 1800  # stała sprężystości sprężyny 1 [N/m]
        self.k2 = 265  # stała sprężystości sprężyny 2 (tłumika) [N/m]
        self.c2 = 30  # tłumienie [Ns/m]
        self.m2 = 43  # masa objektu 2 [kg]
        self.F1_amplitude = 20  # amplituda siły F1 [N]
        self.DUMP = True  # czy uwzględniamy objekt 2 (tłumik) czy nie
    
    # Funkcja opisująca układ równań różniczkowych
    def model(self, y, t):
        x1, v1, x2, v2 = y

        # Równania ruchu dla obiektu 1
        dx1dt = v1
        dv1dt = (self.F1_amplitude * np.sin(t) - self.k1 * x1 - (self.c2 * (v1 - v2) + self.k2 * (x1 - x2) if self.DUMP else 0)) / self.m1

        # Równania ruchu dla obiektu 2 (tłumik drgań)
        dx2dt = v2
        dv2dt = (self.c2 * (v1 - v2) + self.k2 * (x1 - x2)) / self.m2 if self.DUMP else 0

        return [dx1dt, dv1dt, dx2dt, dv2dt]
    
    def generate_solution(self):
        # Warunki początkowe
        y0 = [0, 0, 0, 0]

        # Czas symulacji
        self.t = np.linspace(0, 1000, 100000)
        # Rozwiązanie układu równań różniczkowych
        self.solution = odeint(self.model, y0, self.t)

    def read_y(self, time):
        # Indeks odpowiadający czasowi
        index = np.argmax(self.t >= time)

        # Odczytanie odchylenia dla danego czasu dla obiektu 1 i obiektu 2
        y_obj_1 = self.solution[index, 0]
        y_obj_2 = self.solution[index, 2]

        return y_obj_1, y_obj_2

    def find_optimal_params(self, search_range):
        best_m2, best_k2, best_c2 = None, None, None
        best_odchylenie = float('inf')

        for m2_test in search_range['m2']:
            for k2_test in search_range['k2']:
                for c2_test in search_range['c2']:
                    # Ustaw aktualne parametry tłumika
                    self.m2 = m2_test
                    self.k2 = k2_test
                    self.c2 = c2_test

                    # Przeprowadź symulację
                    self.generate_solution()

                    # Odczytaj odchylenie dla danego czasu
                    y_obj_1, y_obj_2 = self.read_y(0.06)

                    # Ocen skuteczność tłumienia
                    odchylenie_test = np.abs(y_obj_2)

                    if odchylenie_test < best_odchylenie:
                        best_m2, best_k2, best_c2 = m2_test, k2_test, c2_test
                        best_odchylenie = odchylenie_test

        print(f"Najskuteczniejsze parametry tłumika: m2 = {best_m2} kg, k2 = {best_k2} N/m, c2 = {best_c2} Ns/m")
        return best_m2, best_k2, best_c2

# Zakres poszukiwań
#search_range = {'m2': [5, 10, 15], 'k2': [50, 100, 150], 'c2': [10, 20, 30]}

# Inicjalizacja obiektu Solution
solution_obj = Solution()

# Znajdź optymalne parametry tłumika
#best_m2, best_k2, best_c2 = solution_obj.find_optimal_params(search_range)



