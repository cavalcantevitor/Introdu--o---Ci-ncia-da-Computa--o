# ----- QUESTÃO 9 -----

# Coletando dados do usuário
h1, m1, h2, m2 = input().split()
h1, m1, h2, m2 = [int(h1), int(m1), int(h2), int(m2)]

# Definindo variáveis que serão
# utilizadas dentro do loop
horas = 0
minutos = 0

# Calculando a duração do jogo
if (h2 > h1):
    if (m2 > m1):
        horas = h2 - h1
        minutos = m2 - m1
        print(f'O jogo durou {horas} hora(s) e {minutos} minuto(s).')
    elif (m1 > m2):
        # Nesse caso, subtraímos 1 unidade da hora pois,
        # como os minutos são maiores que as horas,
        # não passou uma hora completa, por isso diminuímos
        # uma unidade de hora
        horas = h2 - h1 - 1
        minutos = m2 - m1 + 60
        print(f'O jogo durou {horas} hora(s) e {minutos} minuto(s).')
    else:
        horas = h2 - h1
        minutos = m2 - m1
        print(f'O jogo durou {horas} hora(s) e {minutos} minuto(s).')
elif (h1 > h2):
    if (m2 > m1):
        # Aqui, como o início é maior que o fim,
        # somamos 24h para que não tenha horário negativo
        horas = h2 - h1 + 24
        minutos = m2 - m1
        print(f'O jogo durou {horas} hora(s) e {minutos} minuto(s).')
    elif (m1 > m2):
        # Nessa parte, seguindo a lógica da primeira condição
        # temos que subtrair uma unidade. Mas como estamos falando
        # de um horário inicial cuja hora é maior em módulo que o
        # horário final, precisamos diminuir uma unidade das 24h que adicionamos
        # para não haver hora negativa
        horas = h2 - h1 + 23
        minutos = m2 - m1 + 60
        print(f'O jogo durou {horas} hora(s) e {minutos} minuto(s).')
    else:
        horas = h2 - h1 + 24
        minutos = m2 - m1
        print(f'O jogo durou {horas} hora(s) e {minutos} minuto(s).')
elif (h1 == h2):
    if (m2 > m1):
        # E aqui, as horas sempre serão 24 pois,
        # como o relógio que estamos trabalhando é de 24h,
        # então se as horas forem iguais, então é porque se passaram 24h
        horas = 24
        minutos = m2 - m1
        print(f'O jogo durou {horas} hora(s) e {minutos} minuto(s).')
    elif (m1 > m2):
        # Nesse bloco, por fim, seguimos a mesma lógica de antes diminuindo
        # 1 hora do total, pois, como os minutos iniciais são maiores que
        # os finais, significa que uma hora inteira não foi concluída ainda
        horas = 24 - 1
        minutos = m2 - m1 + 60
        print(f'O jogo durou {horas} hora(s) e {minutos} minuto(s).')
    else:
        horas = 24
        minutos = m2 - m1
        print(f'O jogo durou {horas} hora(s) e {minutos} minuto(s).')