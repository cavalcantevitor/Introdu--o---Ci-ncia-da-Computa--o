# ----- QUESTÃO 1 -----

# Coletando informação do usuário
numero = int(input())

# Verificando se o número é par ou ímpar
if (numero % 2 == 0):
  print(f"{numero} é par")
  print(f"{numero + 2}")
else:
  print(f"{numero} é ímpar")
  print(f"{numero + 2}")