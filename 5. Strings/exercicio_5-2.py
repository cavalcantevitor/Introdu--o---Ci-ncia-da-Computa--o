frase = input()

nova_frase = ''

for letra in frase:
    if letra.lower() not in 'aeiouáéíóú ':
        letra = "p"
    nova_frase += letra

print(nova_frase)
