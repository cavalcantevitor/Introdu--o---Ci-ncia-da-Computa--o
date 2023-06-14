string = input()


def capitalization(text):

    capital_letter = True
    new_string = ""

    for letter in text:
        if capital_letter and letter not in " ":
            letter = letter.upper()
            capital_letter = False
        if letter in ".":
            capital_letter = True
        new_string += letter

    return print(new_string)


capitalization(string)
