import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("dielectric_paraelectric_data.csv")

T = data["Temperature_K"]
epsilon = data["Permittivity"]
loss = data["Loss_Tangent"]

# Plot 1: Permittivity vs Temperature
plt.figure()
plt.plot(T, epsilon, marker="o")
plt.xlabel("Temperature (K)")
plt.ylabel("Permittivity")
plt.title("Quantum Paraelectric Behavior")
plt.grid()
plt.show()

# Plot 2: Loss tangent vs Temperature
plt.figure()
plt.plot(T, loss, marker="s", color="red")
plt.xlabel("Temperature (K)")
plt.ylabel("Loss Tangent")
plt.title("Dielectric Loss vs Temperature")
plt.grid()
plt.show()
