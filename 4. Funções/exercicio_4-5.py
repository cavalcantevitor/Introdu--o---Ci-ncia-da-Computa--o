n = int(input())

def soma_dos_pares(n):
    i = 0
    soma = 0

    while i <= n-2:
        if (i % 2 == 0):
            soma = i + soma
        i = i + 1
    
    if n >= 0:
        return print(f'{soma}')
    else:
        return print(f'{-1}')

soma_dos_pares(n)