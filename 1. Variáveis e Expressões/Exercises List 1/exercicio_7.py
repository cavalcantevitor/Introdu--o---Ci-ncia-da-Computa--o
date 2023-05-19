# ----- Questão 7 ----- 

# Criar um programa que leia o valor de um depósito
# e o valor da taxa de juros mensal. 
# Calcular e imprimir o valor do rendimento 
# e o valor total depois do rendimento para o primeiro mês.

# Coletando input do usuário
deposito = float(input())
taxa_de_juros = float(input()) / 100

# Processando dados recebidos
rendimento = deposito * taxa_de_juros
montante = deposito + rendimento

# Imprimindo o resultado
print('%.2f' %rendimento)
print('%.2f' %montante)