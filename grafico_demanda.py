import numpy as np
import matplotlib.pyplot as plt

# Parámetros del modelo
K = 40000  # Capacidad máxima del mercado (número de hogares)
r = 0.5  # Tasa de crecimiento
t0 = 5  # Tiempo medio para alcanzar la mitad de K (años)

# Vector de tiempo (en años)
t = np.linspace(0, 10, 100)  # Desde 0 hasta 10 años, 100 puntos


# Función de crecimiento logístico
def P(t):
    return K / (1 + np.exp(-r * (t - t0)))


# Cálculo de P(t) para cada valor de t
Pt = P(t)

# Creación de la gráfica
plt.figure(figsize=(10, 6))
plt.plot(t, Pt, label='Demanda proyectada P(t)', color='blue', linewidth=2)
plt.title('Proyección de la Demanda utilizando el Modelo de Crecimiento Logístico', fontsize=14)
plt.xlabel('Tiempo (años)', fontsize=12)
plt.ylabel('Demanda P(t) (número de hogares)', fontsize=12)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
