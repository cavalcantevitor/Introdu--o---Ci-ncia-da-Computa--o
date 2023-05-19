# Definir quantos alunos tem a turma
n = int(input())

# Definindo variáveis
i = 0
aprovados = 0
soma = 0
notas_turma = []

while i < n:
    # Ler 3 notas
    # e o número de faltas de um número n de alunos
    v1, v2, v3, v4 = input().split()
    valores = [float(v1), float(v2), float(v3), float(v4)]

    soma = 0

    for valor in valores:
        soma = soma + valor

    # Calculando a média
    media = (soma - valores[3]) / 3

    # Guardando os valores
    notas_turma.append(media)

    # Validar se ele passou na matéria baseado nas
    # notas E TAMBÉM nas faltas
    if (media >= 5 and valores[3] <= 16):
        print(f'{media:.1f} Aprovado')

        # Contar quantos foram aprovados
        aprovados = aprovados + 1
    elif (media > 3 and media < 5 and valores[3] <= 16):
        print(f'{media:.1f} Exame')
    elif (media < 3 or valores[3] > 16):
        print(f'{media:.1f} Reprovado')

    i = i + 1

# Calcular a média da turma
soma_turma = 0
media_turma = 0

for notas in notas_turma:
    soma_turma = notas + soma_turma

media_turma = soma_turma / n

# Imprimir em tela a média da turma e o numero de aprovados
print(f'{media_turma:.1f} {aprovados}')
