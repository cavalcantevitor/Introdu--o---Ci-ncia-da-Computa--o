# Obtendo o número de figurinhas de Raphael
m, n = input().split()
m, n = [int(m), int(n)]

# Definindo variáveis
i = 1
mdc = 1
maior_num_cartas = 1

if (m > n):
    maior_num_cartas = m
elif (n > m):
    maior_num_cartas = n
else:
    maior_num_cartas = n

while (i <= maior_num_cartas):
    if (n % i == 0 and m % i == 0):
        if (i > mdc):
            mdc = i
        i = i + 1
    else:
        i = i + 1

print(mdc)
