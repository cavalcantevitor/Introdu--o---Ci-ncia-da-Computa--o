# Recebendo o número de meses desejado pelo usuário
n = int(input())

# Definindo o ponto inicial da série de Fibonacci
fn = 1

# Definindo fatorial
f = 1

# Definindo variável contadora
i = 3
j = 3
k = 1

# Calculando a quantidade de casais após n meses
if (n == 1 or n == 2):
    fn = 1
    # print(fn)
elif (n > 2):
    fn_ultimo = 1
    fn_penultimo = 1
    while (i <= n):
        fn = fn_ultimo + fn_penultimo

        fn_penultimo = fn_ultimo
        fn_ultimo = fn
        i = i + 1


# Calculando a quantidade de casais após n + 1 meses
fn1_ultimo = 1
fn1_penultimo = 1
while (j <= (n + 1)):
    fn1 = fn1_ultimo + fn1_penultimo

    fn1_penultimo = fn1_ultimo
    fn1_ultimo = fn1
    j = j + 1

while (k <= n):
    f = f * k
    k = k + 1

# Imprimindo em tela de acordo com as condições exigidas
if (fn % 2 == 0):
    print(f'{fn} {f} {fn1 - fn}')
else:
    print(f'{fn} {f}')
