frase = str(input())


def descriptografador(texto):

    chave_secreta = ""

    frase_sem_espaços = texto.split()

    for palavra in frase_sem_espaços:
        chave_secreta = chave_secreta + palavra[2]

    return print(f'{chave_secreta}')


descriptografador(frase)
