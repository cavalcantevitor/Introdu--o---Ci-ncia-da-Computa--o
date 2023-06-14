string = input()

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_alphabet = alphabet.lower()

new_string = ""

for letter in string:
    if letter in alphabet:
        new_string += "U"
    if letter in lower_alphabet:
        new_string += "L"
    if letter in " ":
        new_string += "W"
    if letter in "0123456789":
        new_string += "D"

print(new_string)
