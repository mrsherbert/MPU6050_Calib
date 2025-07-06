import matplotlib.pyplot as plt
import numpy as np
import math
from sklearn.metrics import mean_squared_error


# Valores pitch
x = [1.00,#0°
     29.59,#30°
     58.23,#60°
     87.34,#90° 
     9.31,#10°
     19.10,#20°
     38.11,#40°
     48.79,#50°
     68.71,#70°
     78.78]#80° # Valores de X encontrados
y = [0,#0°
     30,#30°
     60,#60°
     90,#90° 
     10,#10°
     20,#20°
     40,#40°
     50,#50°
     70,#70°
     80]#80° # Valores de X desejados


'''
# Valores Roll
x = [2.50,#0°
     31.18,#30°
     62.17,#60°
     88.82,#90° 
     10.81,#10°
     19.64,#20°
     40.04,#40°
     50.53,#50°
     71.84,#70°
     81.98]#80° # Valores de X encontrados
y = [0,#0°
     30,#30°
     60,#60°
     90,#90° 
     10,#10°
     20,#20°
     40,#40°
     50,#50°
     70,#70°
     80]#80° # Valores de X desejados
'''

y_plt = np.linspace(0, 90, 1000)
x_plt = y_plt
n = len(x)  # Número de amostras
m = 1       # Grau do polinômio de ajuste
nu = n - m - 1

sumx = 0
sumy = 0
sumxy = 0
sumxx = 0

# Somatórios
for i in range(n):
    sumx += x[i]
    sumy += y[i]
    sumxy += x[i] * y[i]
    sumxx += x[i] * x[i]

mediay = sumy / n  # Média de y

# Coeficiente angular e linear
alfa = (n * sumxy - sumx * sumy) / (n * sumxx - sumx * sumx)
ro = (sumy * sumxx - sumxy * sumx) / (n * sumxx - sumx * sumx)

sy = 0
syx = 0

# Cálculo dos desvios
for i in range(n):
    sy += (y[i] - mediay) ** 2
    syx += (y[i] - ro - alfa * x[i]) ** 2

sy = math.sqrt(sy / (n - 1))
syx = math.sqrt(syx / nu)

salfa = math.sqrt((n * syx ** 2) / (n * sumxx - sumx * sumx))
sro = math.sqrt((syx ** 2 * sumxx) / (n * sumxx - sumx * sumx))

mse = mean_squared_error(x,y)
print(f"O Erro Quadrático Médio (MSE) é: {mse}")
print(f"O valor de ro = {ro:.4f}")
print(f"O valor de alfa = {alfa:.4f}")
print(f"A média de y é = {mediay:.4f}")
print(f"O valor s(y) é = {sy:.4f}")
print(f"O valor s(y,x) é = {syx:.4f}")
print(f"O valor s(alfa) é = {salfa:.4f}")
print(f"O valor s(ro) é = {sro:.4f}")
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