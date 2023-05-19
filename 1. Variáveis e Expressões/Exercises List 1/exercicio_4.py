# ----- Questão 4 ----

# Faça um programa que leia 5 números reais e calcule a média ponderada desses números.
# Calcule e imprima a média m (com 3 casas decimais) usando a fórmula:

# mp =(n1x1 + n2x2 + n3x3 + n4x4 + n5x5)/15

# Coletando input do usuário
n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
n5 = float(input())

# Processando as informações
mp = (n1*1 + n2*2 + n3*3 + n4*4 + n5*5)/15

# Imprimindo resultado
print("%.3f" %mp)