import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.title("Grafica de prueba")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.grid()

plt.savefig("grafica.png")

