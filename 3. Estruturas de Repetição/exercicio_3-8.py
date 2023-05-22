# Variáveis
i = 0
soma = 0
media = 0
maior = -999999999
key = True

# Processando
while (key):
    entrada = int(input())

    if (entrada != 0):
        soma = entrada + soma
        i = i + 1
        media = soma / i
        if (entrada > maior):
            maior = entrada
    elif (entrada == 0 and i > 0):
        key = False
    elif (entrada == 0 and i == 0):
        key = False
        maior = entrada

# Imprimindo resultados em tela
print(f'{i}')
print(f'{maior}')
print(f'{media:.2f}')
