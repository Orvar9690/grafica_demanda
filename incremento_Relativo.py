# Datos necesarios para los gráficos
years = [1, 2, 3, 4, 5]
demand_percentages = [26.89, 37.75, 50, 62.23, 73.1]  # Porcentajes acumulados
increment_relative = [10.86, 12.25, 12.23, 10.87]  # Incrementos relativos entre años
absolute_demand = [4482, 6291, 8333, 10373, 12185]  # Demanda absoluta en hogares
total_capacity = 16667  # Capacidad total del mercado

import matplotlib.pyplot as plt
import numpy as np

# Incremento relativo año a año
plt.figure(figsize=(10, 6))
plt.bar(years[1:], increment_relative, color='orange', alpha=0.8)
plt.title('Incremento Relativo Año a Año', fontsize=14)
plt.xlabel('Año', fontsize=12)
plt.ylabel('Incremento Relativo (%)', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(years[1:])
plt.tight_layout()
plt.show()