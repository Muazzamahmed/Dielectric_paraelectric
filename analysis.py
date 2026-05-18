import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Load dataset
data = pd.read_csv("dielectric_paraelectric_data.csv")

T = data["Temperature_K"].values
epsilon = data["Permittivity"].values

# ----------------------------
# Curie–Weiss law model
# ε = C / (T - Tc)
# ----------------------------
def curie_weiss(T, C, Tc):
    return C / (T - Tc)

# Initial guess
initial_guess = [1e5, 50]

# Fit data
params, covariance = curve_fit(curie_weiss, T, epsilon, p0=initial_guess)

C_fit, Tc_fit = params

# Smooth curve for plotting
T_fit = np.linspace(min(T)+1, max(T), 300)
epsilon_fit = curie_weiss(T_fit, C_fit, Tc_fit)

# ----------------------------
# Plot results
# ----------------------------
plt.figure()
plt.scatter(T, epsilon, label="Data", color="blue")
plt.plot(T_fit, epsilon_fit, label=f"Fit: Tc={Tc_fit:.2f} K", color="red")

plt.xlabel("Temperature (K)")
plt.ylabel("Permittivity")
plt.title("Curie–Weiss Fit (Quantum Paraelectric Model)")
plt.legend()
plt.grid()
plt.show()

print("Fitted Parameters:")
print("C =", C_fit)
print("Tc =", Tc_fit)
