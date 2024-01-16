import numpy as np

# Redefine given data due to reset of execution state
m1 = 50  # Mass m1 in kg
k1 = 1800  # Spring constant k1 in N/m
m2 = 2  # Mass m2 in kg (damper mass)
p0 = 2 * np.pi  # Corrected operating frequency in rad/s
k2 = m2 * p0**2  # Calculated spring constant k2 based on B1 = 0 condition


# Given force
F = 50  # Force in N

# Since p is equal to p0 in this case, we can directly use p0 for calculations
p = p0


# Calculate B1 and B2 using the provided formulas
denominator = m1 * m2 * p**4 - (m1 * k2 + (k1 + k2) * m2) * p**2 + k1 * k2
b1 = (k2 - m2 * p**2) / denominator * F
b2 = k2 / denominator * F
# Output all the given data, calculated k2, and the calculated frequencies
print(
    f"Masa 1: {m1}\nSprężystość sprężyny 1: {k1}\nMasa 2: {m2}, {p0}\nSprężystość sprężyny 2: {k2}\nAmplituda 1: {b1}\nAmplituda 2: {b2}"
)
