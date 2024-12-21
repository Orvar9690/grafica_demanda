import matplotlib.pyplot as plt
import numpy as np

# Datos extraídos de la interpretación
years = [1, 2, 3, 4, 5]
demand_percentages = [26.89, 37.75, 50, 62.23, 73.1]  # Porcentajes de la demanda inicial alcanzados
relative_growth = [10.85, 12.25, 12.23, 10.87]  # Incrementos relativos entre años

# Crear la gráfica de demanda acumulada
plt.figure(figsize=(10, 6))
plt.plot(years, demand_percentages, marker='o', label='Porcentaje acumulado de la demanda (%)', color='blue', linewidth=2)

# Agregar datos adicionales
for i, value in enumerate(demand_percentages):
    plt.text(years[i], value + 1, f"{value}%", ha='center', fontsize=10)

# Configuración del gráfico
plt.title('Crecimiento Acumulado de la Demanda', fontsize=14)
plt.xlabel('Año', fontsize=12)
plt.ylabel('Porcentaje de la Demanda Total (%)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(years)
plt.ylim(0, 80)  # Ajustar límites para claridad
plt.legend(fontsize=12)
plt.tight_layout()

# Mostrar el gráfico
plt.show()