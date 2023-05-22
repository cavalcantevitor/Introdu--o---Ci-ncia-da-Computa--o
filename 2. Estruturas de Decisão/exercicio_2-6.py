# ----- QUESTÃO 6 -----

# Coletando input() do usuário
m, d = input().split()
m, d = [int(m), int(d)]

# Validando e processando entrada
if (m == 1 or m == 3 or m == 5 or m ==7 or m == 8 or m == 10 or m == 12):
    if (d > 5):
        print(6)
    else:
        print(5)
elif (m == 2):
    if (d == 1):
        print(4)
    elif (d > 1):
        print(5)
elif (m == 4 or m == 6 or m == 9 or m == 11):
    if (d > 6):
        print(6)
    else:
        print(5)