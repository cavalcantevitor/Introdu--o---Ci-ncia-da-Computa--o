# ----- QUESTÃO 7 -----

# Coletando input() do usuário
peso = float(input())
altura = float(input())

# Calculando o IMC
imc = peso / altura ** 2

# Calculando peso sobressalente
peso_sobressalente = peso - (24.9 * (altura ** 2))

# Classificando o IMC de acordo com as regras
if (imc < 18.5):
    print(f'{imc:.2f}')
    print("Baixo peso")
elif (imc > 18.5 and imc <= 24.9):
    print(f'{imc:.2f}')
    print("Peso normal")
elif (imc > 24.9 and imc <= 29.9):
    print(f'{imc:.2f}')
    print("Sobrepeso")
    print('%.2f' % peso_sobressalente)
elif (imc > 29.9 and imc <= 34.9):
    print(f'{imc:.2f}')
    print("Obesidade grau I")
    print('%.2f' % peso_sobressalente)
elif (imc > 34.9 and imc < 39.9):
    print(f'{imc:.2f}')
    print("Obesidade grau II")
    print('%.2f' % peso_sobressalente)
else:
    print(f'{imc:.2f}')
    print("Obesidade grau III")
    print('%.2f' % peso_sobressalente)