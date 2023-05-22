n = int(input())
m = 1
# key = True
numero = n * m + 1
divisor = 2
primo = True

while primo:
    if (numero % divisor == 0):
        primo = False
    elif (numero % divisor != 0):
        while (divisor < numero):
            divisor = divisor + 1

    m = m + 1

print(m)
