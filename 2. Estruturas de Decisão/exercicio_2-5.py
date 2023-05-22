# ----- QUESTÃO 5 -----

# Coletando input() do usuário
string1 = input();
string2 = input();

# Validando as subsequências
if (string1 == string2):
    print(-1)
else:
    if (string1 > string2):
        print(len(string1))
    else:
        print(len(string2))