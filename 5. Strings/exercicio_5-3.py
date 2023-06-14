palavras = str(input())
palavras_separadas = palavras.lower().split()
palavra1, palavra2 = [str(palavras_separadas[0]), str(palavras_separadas[1])]

if palavra1 > palavra2:
    print(f'A')
else:
    print(f'B')
