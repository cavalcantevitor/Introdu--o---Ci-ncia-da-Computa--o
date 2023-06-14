string_1 = input()
string_2 = input()

letters_eaten = ""

for letter in string_1:
    if letter in string_2:
        letters_eaten = letters_eaten
    if letter not in string_2:
        letters_eaten += letter


def count(letters):

    counter = 0

    for letter in letters:
        if letter.lower() in "john":
            counter += 1
    return counter


result_1 = count(letters_eaten)
result_2 = count(string_2)

print(f'{result_1} {result_2}')
