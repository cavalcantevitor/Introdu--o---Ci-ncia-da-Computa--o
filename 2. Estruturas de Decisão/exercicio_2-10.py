# ----- QUESTÃO 10 -----

# Coletando dados do usuário
t1, v1, t2, v2 = input().split()
t1, v1, t2, v2 = [int(t1), int(v1), int(t2), int(v2)]

penalidade_tempo1 = 0
penalidade_tempo2 = 0
penalidade_velocidade1 = 0
penalidade_velocidade2 = 0

# ----- Processamento das informações -----

# Calculando as penalidades de tempo no trecho 1
if (t1 > 1800):
    penalidade_tempo1 = (t1 - 1800) * -1
elif (t1 < 1800):
    penalidade_tempo1 = (-1800 + t1) * 2

# Calculando as penalidade de velocidade no trecho 1
if (v1 > 60):
    penalidade_velocidade1 = (v1 - 60) * -10
elif (v1 < 60):
    penalidade_velocidade1 = 0

# Calculando as penalidades de tempo no trecho 2
if (t2 > 3600):
    penalidade_tempo2 = (t2 - 3600) * -1
elif (t1 < 3600):
    penalidade_tempo2 = (-3600 + t2) * 2 

# Calculando as penalidades de velocidade no trcho 2
if (v2 > 40):
    penalidade_velocidade2 = (v2 - 40) * -20
elif (v2 < 40):
    penalidade_velocidade2 = 0
# ----- Resultados ------
print(f'{penalidade_tempo1}')
print(f'{penalidade_tempo1 + penalidade_velocidade1}')
print(f'{penalidade_tempo2}')
print(f'{penalidade_tempo2 + penalidade_velocidade2}')
print(f'{penalidade_tempo1 + penalidade_tempo2}')
print(f'{penalidade_tempo1 + penalidade_tempo2 + penalidade_velocidade1 + penalidade_velocidade2}')