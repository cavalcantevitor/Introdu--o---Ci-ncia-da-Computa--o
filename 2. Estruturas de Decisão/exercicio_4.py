# ----- QUESTÃO 4 -----

# Coletando dados do usuário
a, b = input().split()
a, b = [int(a), int(b)]

# Avaliando os passos
if ((a - b) > 1 or (b - a) > 1 or b < 1 or a > b):
  print(f'{a} {b} errados')
elif ((a - b) <=1 or (b - a) <= 1):
  print(f'{a} {b} ok')