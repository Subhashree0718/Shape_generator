import numpy as np
import matplotlib.pyplot as plt

# Generate values for t
t = np.linspace(0, 2 * np.pi, 1000)

# Heart shape parametric equations
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

# Create plot
plt.figure(figsize=(6, 6))
plt.plot(x, y, 'r', linewidth=2)

# Add basic labels
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Heart Shape")

# Simple grid and axis lines
plt.grid(True, linestyle='--', linewidth=0.5)
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

plt.show()
