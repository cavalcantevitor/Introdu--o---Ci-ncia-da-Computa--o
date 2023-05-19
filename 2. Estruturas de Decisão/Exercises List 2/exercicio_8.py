# ----- QUESTÃO 8 -----

# Coletando valores do usuário
a = float(input())
b = float(input())
c = float(input())

lado_maior = 0
lado1 = 0
lado2 = 0

# Ordenando os lados
if (a > b and a > c): 
    lado_maior = a
    lado1 = b
    lado2 = c
elif (a > b and a <= c or b > a and b < c or c > a and c > b):
    lado_maior = c
    lado1 = a
    lado2 = b
elif (b > a and b > c):
    lado_maior = b
    lado1 = a
    lado2 = c
elif (a == b and b == c):
    lado_maior = a
    lado1 = b
    lado2 = c
elif (a >= c and a >= b):
    lado_maior = a
    lado1 = c
    lado2 = b

# Avaliando e classificando o triangulo
# conforme o tamanho dos lados

if (lado_maior >= (lado1 + lado2)):
    print('NAO FORMA TRIANGULO')
elif (lado_maior ** 2 == lado1 ** 2 + lado2 ** 2):
    print('TRIANGULO RETANGULO')
elif (lado_maior == lado1 and lado_maior == lado2):
    print('TRIANGULO EQUILATERO')
elif (lado_maior == lado1 or lado1 == lado2 or lado_maior == lado2):
    print('TRIANGULO ISOSCELES')
else:
    print('TRIANGULO ACUTANGULO OU OBTUSANGULO')