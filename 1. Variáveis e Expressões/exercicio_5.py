# ----- Questão 5 -----

# Em épocas de pouco dinheiro, os comerciantes 
# estão procurando aumentar suas vendas oferecendo desconto. 
# Faça um programa que possa entrar com o valor de um produto 
# e imprima o novo valor tendo em vista que o desconto foi de 6%.

# Coletando o preço inicial
preco_inicial = float(input())

# Processando o preço
preco_com_desconto = preco_inicial - preco_inicial*0.06

# Imprimindo o preço final
print("%.2f" %preco_com_desconto)