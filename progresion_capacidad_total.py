# Datos necesarios para los gráficos
years = [1, 2, 3, 4, 5]
demand_percentages = [26.89, 37.75, 50, 62.23, 73.1]  # Porcentajes acumulados
increment_relative = [10.86, 12.25, 12.23, 10.87]  # Incrementos relativos entre años
absolute_demand = [4482, 6291, 8333, 10373, 12185]  # Demanda absoluta en hogares
total_capacity = 16667  # Capacidad total del mercado

import matplotlib.pyplot as plt
import numpy as np

# Progresión hacia la capacidad total del mercado
plt.figure(figsize=(10, 6))
plt.plot(years, np.array(absolute_demand) / total_capacity * 100, marker='o', color='green', linewidth=2)
plt.axhline(y=100, color='red', linestyle='--', label='Capacidad total del mercado (100%)')
plt.title('Progresión Hacia la Capacidad Total del Mercado', fontsize=14)
plt.xlabel('Año', fontsize=12)
plt.ylabel('Porcentaje de la Capacidad Total (%)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=12)
plt.tight_layout()
plt.show()