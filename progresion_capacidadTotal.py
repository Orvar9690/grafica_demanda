
# Datos necesarios para los gráficos
years = [1, 2, 3, 4, 5]
demand_percentages = [26.89, 37.75, 50, 62.23, 73.1]  # Porcentajes acumulados
increment_relative = [10.86, 12.25, 12.23, 10.87]  # Incrementos relativos entre años
absolute_demand = [4482, 6291, 8333, 10373, 12185]  # Demanda absoluta en hogares
total_capacity = 16667  # Capacidad total del mercado

import matplotlib.pyplot as plt
import numpy as np

# Comparación entre Progresión y Capacidad Total
plt.figure(figsize=(10, 6))
plt.plot(years, absolute_demand, marker='o', color='blue', linewidth=2, label='Demanda Proyectada')
plt.axhline(y=total_capacity, color='red', linestyle='--', label=f'Capacidad Máxima ({total_capacity})')
plt.title('Comparación de Progresión vs. Capacidad Total del Mercado', fontsize=14)
plt.xlabel('Año', fontsize=12)
plt.ylabel('Demanda (Hogares)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=12)
plt.tight_layout()
plt.show()