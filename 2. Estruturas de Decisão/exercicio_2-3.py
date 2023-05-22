# ----- QUESTÃO 3 -----

# Coletando dados do usuário
cargo = input()
tempo_de_servico = int(input())
salario_atual = float(input())

# Avaliando o cargo
if (salario_atual < 1039):
    print('Salário inválido!')
elif (cargo == 'Gerente'):
    if (tempo_de_servico <= 3 and tempo_de_servico > 0):
        novo_salario = salario_atual * 1.12
        reajuste = novo_salario - salario_atual

        print('%.2f' %reajuste)
        print('%.2f' %novo_salario)
    elif (tempo_de_servico > 3 and tempo_de_servico <= 6):
        novo_salario = salario_atual * 1.13
        reajuste = novo_salario - salario_atual

        print('%.2f' %reajuste)
        print('%.2f' %novo_salario)
    elif (tempo_de_servico > 6):
            novo_salario = salario_atual * 1.15
            reajuste = novo_salario - salario_atual

            print('%.2f' %reajuste)
            print('%.2f' %novo_salario)
elif (cargo == 'Engenheiro'):
    if (tempo_de_servico <= 3 and tempo_de_servico > 0):
            novo_salario = salario_atual * 1.07
            reajuste = novo_salario - salario_atual

            print('%.2f' %reajuste)
            print('%.2f' %novo_salario)
    elif (tempo_de_servico > 3 and tempo_de_servico <= 6):
            novo_salario = salario_atual * 1.11
            reajuste = novo_salario - salario_atual

            print('%.2f' %reajuste)
            print('%.2f' %novo_salario)
    elif (tempo_de_servico > 6):
        novo_salario = salario_atual * 1.14
        reajuste = novo_salario - salario_atual

        print('%.2f' %reajuste)
        print('%.2f' %novo_salario)
else: 
    if (tempo_de_servico > 0):
        novo_salario = salario_atual * 1.05
        reajuste = novo_salario - salario_atual

        print('%.2f' %reajuste)
        print('%.2f' %novo_salario)