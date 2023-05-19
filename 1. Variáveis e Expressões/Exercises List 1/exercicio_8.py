# ----- Questão 8 -----

# Leia quatro valores correspondentes 
# aos eixos x e y de dois pontos quaisquer no plano: (x1, y1) e (x2, y2)
# e calcule a distância entre eles, 
# mostrando 4 casas decimais após a vírgula, segundo a fórmula:
# ((x2 − x1)^2 + (y2 − y1)^2)^1/2

# Leia também um número complexo z = a + bj e 
# calcule seu módulo |z| (distância até a origem), 
# mostrando 4 casas decimais após a vírgula, usando a fórmula:
# |z| = ((a^2 + b^2))^1/2

# Note que Python possui complex como tipo de dados. 
# Um número complexo tem um componente real e um componente imaginário, 
# ambos representados pelo tipo float em Python (é possível acessá-los separadamente).

# Importando números complexos
import cmath

# Coletando coordenadas 
x1, y1 = input().split()
x2, y2 = input().split()
x1, y1 = [float(x1), float(y1)]
x2, y2 = [float(x2), float(y2)]

# Coletando as partes real e imaginária do número complexo
z = complex(input())

# Calculando a distância entre dois pontos
d = ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)

# Calculando o módulo do número complexo
m = (z.real**2 + z.imag**2)**(1/2)

# Imprimindo os resultados
print("%.4f" %d)
print("%.4f" %m)