
# Datos necesarios para los gráficos
years = [1, 2, 3, 4, 5]
demand_percentages = [26.89, 37.75, 50, 62.23, 73.1]  # Porcentajes acumulados
increment_relative = [10.86, 12.25, 12.23, 10.87]  # Incrementos relativos entre años
absolute_demand = [4482, 6291, 8333, 10373, 12185]  # Demanda absoluta en hogares
total_capacity = 16667  # Capacidad total del mercado

import matplotlib.pyplot as plt
import numpy as np

# Gráfico 3: Distribución de crecimiento en porcentajes relativos
plt.figure(figsize=(10, 6))
plt.bar(years, demand_percentages, color='purple', alpha=0.8)
plt.title('Distribución del Crecimiento en Porcentajes Relativos', fontsize=14)
plt.xlabel('Año', fontsize=12)
plt.ylabel('Porcentaje del Total Alcanzado (%)', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(years)
plt.tight_layout()
plt.show()