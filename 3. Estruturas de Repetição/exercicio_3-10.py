# Obtendo input do usuário
n = int(input())

# Definindo variáveis
m = 1
numero = n * m + 1
divisor = 2
primo = True # definindo a propriedade primo como verdadeira

# Iniciando loop para obter "m"
while primo:

    # Validando se número realmente é primo
    if (numero % divisor == 0):
        primo = False

        # Encerrando o loop caso o número seja primo
        break

    # Somando unidades ao divisor
    elif (numero % divisor != 0):
        while (divisor < numero):
            divisor = divisor + 1

    m = m + 1

# Imprimindo "m" na tela
print(m)
