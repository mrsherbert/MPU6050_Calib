import matplotlib.pyplot as plt
import numpy as np
import math

'''
# Calibração Az
x = [0.93, 0.92, 0.94, 0.69, 0.95, 0.91, 0.90, 0.96, 1.09, 0.81,
     0.80, 0.79, 0.65, 0.66, 0.64, 0.67, 0.44, 0.43, 0.42,
     0.12, 0.15, 0.17, 0.13, 0.15, 0.31, 0.30, 0.29,
     0.62, 0.63, 0.72, 0.71, 0.73, 0.89, 0.87, 0.88,
     0.91, 0.92, 0.93, 0.03, 0.05, -0.05, -0.06, -0.07, 
     -0.04, -0.02, -0.01, -0.08, -0.11] # Valores de X encontrados
y = [1.0, 1.0, 1.0, 0.7, 1.0, 1.0, 1.0, 1.0, 1.0, 0.86,
     0.86, 0.86, 0.7, 0.7, 0.7, 0.7, 0.5, 0.5, 0.5,
     0.17, 0.17, 0.17, 0.17, 0.17, 0.34, 0.34, 0.34,
     0.64, 0.64, 0.76, 0.76, 0.76, 0.94, 0.94, 0.94,
     0.94, 0.94, 0.94, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
     0.0, 0.0, 0.0, 0.0 ] # Valores de X desejados
'''

'''
# Calibração Ay
x = [0.20, 0.18, 0.19, 0.35, 0.37, 0.36, 0.34, 0.64, 0.63, 0.62,
     -0.09, 0.75, 0.74, 0.92, 0.93, 0.98, 0.96, 0.97, 0.99,
     -0.03, -0.04, -0.02, -0.20, -0.06, -0.00, -0.05, -0.14, 
     0.47,   0.48,  0.49,  0.46,  0.66,  0.67,  0.68,  0.67,
     0.85,   0.84,  0.86,  0.83,  0.99,  1.01,  0.97,  0.98, 
     0.96,   1.03,  0.93,  0.95] # valores encontrados
y = [0.17,   0.17, 0.17, 0.34, 0.34, 0.34, 0.34, 0.64, 0.64, 
     0.64,    0.0, 0.76, 0.76, 0.94, 0.94, 0.94, 0.98, 0.98, 0.98,
     0.00,   0.00,  0.00,  0.00,  0.00,  0.00,  0.00,  0.00,
     0.50,   0.50,  0.50,  0.50,  0.70,  0.70,  0.70,  0.70,
     0.86,   0.86,  0.86,  0.86,  1.00,  1.00,  1.00,  1.00,
     1.00,   1.00,  1.00,  1.00] # Valores desejados
'''



# Calibração Ax
x = [-0.03, -0.04, -0.05, -0.07, -0.16,  0.05, -0.11, -0.10,  0.52,  0.51, 
     0.53,   0.69,  0.68,  0.70,  0.71,  0.85,  0.86,  1.04,  1.03,  1.01,
     1.00,  1.02,  1.05, 0.18, 0.17, 0.34, 0.35, 0.65, 0.66, 0.75, 0.76, 
     0.96, 0.97, 1.00, 1.01, 1.02] # Valores de X encontrados
y = [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.50, 0.50,
     0.50, 0.70, 0.70, 0.70, 0.70, 0.86, 0.86, 1.00, 1.00, 1.00,
     1.00, 1.00, 1.00, 0.17, 0.17, 0.34, 0.34, 0.64, 0.64, 0.76, 
     0.76, 0.94, 0.94, 0.98, 0.98, 0.98] # Valores de X desejados


'''
# Yaw
x = [-87.52, -56.79, -44.95, -27.95, 0.00, 29.61, 42.25, 56.07, 84.89] # Valores de X encontrados
y = [-90.00, -60.00, -45.00, -30.00, 0.00, 30.00, 45.00, 60.00, 90.00] # Valores de X desejados
'''

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

# Resultados
print(f"O valor de ro = {ro:.4f}")
print(f"O valor de alfa = {alfa:.4f}")
print(f"A média de y é = {mediay:.4f}")
print(f"O valor s(y) é = {sy:.4f}")
print(f"O valor s(y,x) é = {syx:.4f}")
print(f"O valor s(alfa) é = {salfa:.4f}")
print(f"O valor s(ro) é = {sro:.4f}")

y_plt = np.linspace(-0.25, 1.1, 1000)
x_plt = alfa * y_plt + ro

# Criar o gráfico de dispersão
plt.figure(figsize=(10, 6))
plt.plot(x_plt, y_plt)
plt.scatter(x, y, label='Dados')

# Adicionar títulos e legendas
plt.title('Gráfico de Dispersão de X vs Y')
plt.xlabel('Valores de X encontrados')
plt.ylabel('Valores desejados de Y')
plt.legend()
plt.grid(True)

# Exibir o gráfico
plt.show()