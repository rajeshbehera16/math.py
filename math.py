import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-10, 10, 1000)  # For y=x^2, sin(x), cos(x)
x_linear = np.linspace(-10, 10, 100)  # For y=mx+c
y_x2 = x ** 2
y_sinx = np.sin(x)
y_cosx = np.cos(x)
m = 2  # Slope
c = 5  # Intercept
y_mx_c = m * x_linear + c

# Plot the equations
plt.figure(figsize=(10, 6))

# Plot y = x^2
plt.plot(x, y_x2, label=r"$y = x^2$", color="blue")

# Plot y = sin(x)
plt.plot(x, y_sinx, label=r"$y = \sin(x)$", color="green")

# Plot y = cos(x)
plt.plot(x, y_cosx, label=r"$y = \cos(x)$", color="red")

# Plot y = mx + c
plt.plot(x_linear, y_mx_c, label=f"$y = {m}x + {c}$", color="orange")

# Add grid, legend, and labels
plt.grid(True, linestyle="--", alpha=0.7)
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.title("Plot of Mathematical Equations", fontsize=14)
plt.xlabel("x", fontsize=12)
plt.ylabel("y", fontsize=12)
plt.legend(fontsize=12)
plt.tight_layout()

# Show the plot
plt.show()
