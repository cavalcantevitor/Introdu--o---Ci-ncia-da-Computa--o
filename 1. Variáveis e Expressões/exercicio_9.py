# ----- Questão 9 -----

# RELOGIO DIGITAL
# Leia do teclado um valor inteiro x, 
# que é o tempo de duração em segundos de um determinado evento, 
# e informe-o expresso no formato: horash:minutosm:segundoss.

# ENTRADA
# Um único inteiro x.

# SAÍDA
# Imprima o tempo lido em segundos, 
# convertido para horash:minutosm:segundoss, 
# conforme exemplos da tabela abaixo.

# Coletando tempo em segundos
tempo_em_segundos = int(input())

# Separando em horas(h), minutos(m) e segundos(s)
horas = tempo_em_segundos // 3600
minutos = (tempo_em_segundos // 60) - horas * 60
segundos = tempo_em_segundos % 60

# Imprimindo o resultado
print(f"{horas}h:{minutos}m:{segundos}s")   