# Variáveis
i = 0
p = 0
u = 0

# Coletando o número de frases
n = int(input())

# Rodando o loop pelo número de frases recebido
while (i < n):
    string = str(input())

    split_string = string.split()

    for word in split_string:
        for letter in word:
            if "p" == letter.lower():
                p = p + 1
            if "u" == letter.lower():
                u = u + 1

    i = i + 1

print(f'{p} {u}')
