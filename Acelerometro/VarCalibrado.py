import matplotlib.pyplot as plt
import numpy as np
import math
from sklearn.metrics import mean_squared_error

'''
# Calibrado Az
x = [-0.04, -0.05, -0.05,#0°
     0.47, 0.48, 0.49,#30°
     0.84, 0.85, 0.86,#60°
     0.97, 0.98, 0.99,#90° 
     0.13, 0.13, 0.15,#10°
     0.30, 0.31, 0.32,#20°
     0.64, 0.63, 0.62,#40°
     0.74, 0.75,#50°
     0.91, 0.92, 0.93,#70°
     0.96, 0.97, 0.98]#80° # Valores de X encontrados
y = [0.00, 0.00, 0.00,#0°
     0.50, 0.50, 0.50,#30°
     0.86, 0.86, 0.86,#60°
     1.00, 1.00, 1.00,#90° 
     0.17, 0.17, 0.17,#10°
     0.34, 0.34, 0.34,#20°
     0.64, 0.64, 0.64,#40°
     0.76, 0.76,#50°
     0.94, 0.94, 0.94,#70°
     0.98, 0.98, 0.98]#80° # Valores de X desejados
'''

'''
# Calibração Ay
x = [0.00, 0.01, -0.00,#0°
     0.49, 0.50,#30°
     0.84, 0.85, 0.86,#60°
     0.99, 1.00,#90° 
     0.17, 0.16,#10°
     0.34, 0.35,#20°
     0.63, 0.64,#40°
     0.74, 0.75,#50°
     0.94, 0.93,#70°
     0.98, 0.97]#80° # Valores de X encontrados
y = [0.00, 0.00, 0.00,#0°
     0.50, 0.50,#30°
     0.86, 0.86, 0.86,#60°
     1.00, 1.00,#90° 
     0.17, 0.17,#10°
     0.34, 0.34,#20°
     0.64, 0.64,#40°
     0.76, 0.76,#50°
     0.94, 0.94,#70°
     0.98, 0.98]#80° # Valores de X desejados
'''

'''
# Calibração Ax
x = [0.01, 0.02,#0°
     0.50, 0.49,#30°
     0.86, 0.85,#60°
     1.00, 1.01,#90° 
     0.17, 0.18,#10°
     0.34, 0.33, 0.32,#20°
     0.64, 0.64,#40°
     0.72, 0.73, 0.74,#50°
     0.91, 0.92,#70°
     0.98, 0.99]#80° # Valores de X encontrados
y = [0.00, 0.00,#0°
     0.50, 0.50,#30°
     0.86, 0.86,#60°
     1.00, 1.00,#90° 
     0.17, 0.17,#10°
     0.34, 0.34, 0.34,#20°
     0.64, 0.64,#40°
     0.76, 0.76, 0.76,#50°
     0.94, 0.94,#70°
     0.98, 0.98]#80° # Valores de X desejados
'''

'''
# Yaw
x = [-87.52, -56.79, -44.95, -27.95, 0.00, 29.61, 42.25, 56.07, 84.89] # Valores de X encontrados
y = [-90.00, -60.00, -45.00, -30.00, 0.00, 30.00, 45.00, 60.00, 90.00] # Valores de X desejados
'''

y_plt = np.linspace(-0.09, 1.05, 1000)
x_plt = y_plt

mse = mean_squared_error(x,y)
print(f"O Erro Quadrático Médio (MSE) é: {mse}")
# Criar o gráfico de dispersão
plt.figure(figsize=(10, 6))
plt.plot(x_plt, y_plt)
plt.scatter(x, y, label='Dados')

# Adicionar títulos e legendas
plt.title('Gráfico dados calibrados')
plt.xlabel('Valores encontrados')
plt.ylabel('Reta normal')
plt.legend()
plt.grid(True)

# Exibir o gráfico
plt.show()