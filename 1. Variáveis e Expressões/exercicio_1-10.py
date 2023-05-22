# ----- Questão 10 -----

# Troco em Cédulas

# Leia um valor inteiro. A seguir, 
# calcule o menor número de notas possı́veis (cédulas) 
# no qual o valor pode ser decomposto. 
# As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1.
# A seguir mostre o valor lido e a relação de notas necessárias.

# Entrada :

# A entrada contém um valor inteiro N.

# Saı́da:

# Imprima o valor lido e, em seguida, 
# a quantidade mı́nima de notas de cada tipo necessárias, 
# conforme o exemplo fornecido abaixo.

# For example:

# Input
# 576

# Result
# 5 nota(s) de R$ 100,00
# 1 nota(s) de R$ 50,00
# 1 nota(s) de R$ 20,00
# 0 nota(s) de R$ 10,00
# 1 nota(s) de R$ 5,00
# 0 nota(s) de R$ 2,00
# 1 nota(s) de R$ 1,00

# Coletando o valor total
valor_total = int(input())

# Separando esse valor em notas
notas100 = valor_total // 100
notas50 = (valor_total - (notas100*100)) // 50
notas20 = (valor_total - (notas100 * 100) - (notas50 * 50)) // 20
notas10 = (valor_total - (notas100 * 100) - (notas50 * 50) - (notas20 * 20)) // 10
notas5 = (valor_total - (notas100 * 100) - (notas50 * 50) - (notas20 * 20) - (notas10 * 10)) // 5
notas2 = (valor_total - (notas100 * 100) - (notas50 * 50) - (notas20 * 20) - (notas10 * 10) - (notas5 * 5)) // 2
notas1 = (valor_total - (notas100 * 100) - (notas50 * 50) - (notas20 * 20) - (notas10 * 10) - (notas5 * 5) - (notas2 * 2)) // 1

# Imprimindo resultado
print(valor_total)
print(f"{notas100} nota(s) de R$ 100,00")
print(f"{notas50} nota(s) de R$ 50,00")
print(f"{notas20} nota(s) de R$ 20,00")
print(f"{notas10} nota(s) de R$ 10,00")
print(f"{notas5} nota(s) de R$ 5,00")
print(f"{notas2} nota(s) de R$ 2,00")
print(f"{notas1} nota(s) de R$ 1,00")
