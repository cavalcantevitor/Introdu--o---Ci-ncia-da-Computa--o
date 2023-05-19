# ----- QUESTÃO 2 -----

# Coletando informações do usuário
valor_da_compra, parcelas = input().split()
valor_da_compra, parcelas = [float(valor_da_compra), float(parcelas)]

# Avaliando como será efetuada
if (parcelas == 1):
  # Aplicando descontos/juros sobre a compra
  valor_a_pagar = valor_da_compra * 0.95

  # Calculando o valor isolado de cada parcela
  valor_da_prestacao = valor_a_pagar / parcelas
  
  print("%.2f %.2f" %(valor_a_pagar, valor_da_prestacao))
elif (parcelas == 2):
  valor_a_pagar = valor_da_compra * 1
  valor_da_prestacao = valor_a_pagar / parcelas
  
  print("%.2f %.2f" %(valor_a_pagar, valor_da_prestacao))
elif (parcelas == 3):
  valor_a_pagar = valor_da_compra * 1.05
  valor_da_prestacao = valor_a_pagar / parcelas
  
  print("%.2f %.2f" %(valor_a_pagar, valor_da_prestacao))
elif (parcelas == 4):
  valor_a_pagar = valor_da_compra * 1.1
  valor_da_prestacao = valor_a_pagar / parcelas
  
  print("%.2f %.2f" %(valor_a_pagar, valor_da_prestacao))