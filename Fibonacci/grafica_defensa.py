import matplotlib.pyplot as plt
import numpy as np

# 1. Ejemplo de datos (ajusta estos datos después)
meses = ['2025-05', '2025-06', '2025-07']
porcentajes_SRT = [70.83, 90.63, 93.33]
porcentajes_DTS = [0.72, 0.49, 1.32]
porcentajes_FDR = [82.70, 82.12, 57.26]

# 2. Crear figura con 2 subgráficas horizontales
fig, axs = plt.subplots(1, 2, figsize=(12, 4))

# 3. Primera gráfica tipo línea
axs[0].plot(meses, porcentajes_SRT, marker='o', color='royalblue', label='Satisfaction Rate')
for i, v in enumerate(porcentajes_SRT):
    axs[0].text(i, v + 2, f"{v:.2f}%", ha='center', va='bottom', fontsize=9)

axs[0].plot(meses, porcentajes_FDR, marker='o', color='orange', label='FDR')
for i, v in enumerate(porcentajes_FDR):
	axs[0].text(i, v + 2, f"{v:.2f}%", ha='center', va='bottom', fontsize=9)


axs[0].set_ylim(50, 110)
axs[0].set_title('Satisfaction Rate and First Day Resolve (FDR)')
axs[0].set_xlabel('Close Month')
axs[0].set_ylabel('Porcentage (%)')
axs[0].grid(True, linestyle='--', alpha=0.6)
axs[0].legend()

# 4. Segunda gráfica tipo línea
axs[1].plot(meses, porcentajes_DTS, marker='o', color='green', label='Days To Solve')
for i, v in enumerate(porcentajes_DTS):
	axs[1].text(i, v + 0.03, f"{v:.2f}", ha='center', va='bottom', fontsize=9)



axs[1].set_ylim(0.2, 1.4)
axs[1].set_title('Days To Solve (DTS)')
axs[1].set_xlabel('Close Month')
axs[1].set_ylabel('DTS Indicator')
axs[1].grid(True, linestyle='--', alpha=0.6)
axs[1].legend()

plt.tight_layout()
plt.savefig("kpi.png", dpi=100)
plt.close()

print("¡Imagen generada: kpi.png!")

