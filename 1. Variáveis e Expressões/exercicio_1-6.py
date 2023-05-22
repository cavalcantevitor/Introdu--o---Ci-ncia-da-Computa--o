# ----- Questão 6 -----

# Efetuar o cálculo da quantidade de litros de combustível 
# (gasolina) gastos em uma viagem, 
# sabendo-se que o carro faz 14.2 km com um litro (na estrada). 
# Deverão ser lidos o tempo gasto na viagem e a velocidade média. 

# Utilizar as seguintes fórmulas:
# distancia = tempo x velocidade
# litros = distancia / 14.2

# - Entrada -
# Duas entradas com valores reais, um por linha. 
# O primeiro valor é o tempo gasto na viagem (em horas) 
# e o segundo valor é a velocidade média (km/h).

# - Saída -
# O programa deverá apresentar os valores da distância percorrida 
# e a quantidade de litros utilizados na viagem. 
# Observe que as saídas são números reais 
# e apenas a quantidade de litros deve ser formatada com duas casas decimais, 
# ou seja, a distância percorrida não deve ser formatada, conforme os exemplos a seguir. 
# Os valores são apresentados na mesma linha e separados por espaço.

# Coletando os valores da velocidade e da distância
tempo = float(input())
velocidade = float(input())

# Transformando tempo e velocidade em distâcia
distancia = tempo * velocidade

# Obtendo os litros de gasolina gastos na viagem
litros = distancia / 14.2

# Imprimindo o resultado
print("{} {:.2f}".format(distancia, litros))