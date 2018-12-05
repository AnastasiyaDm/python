import random
a = input("Enter the phrase: ")
vowels = "AEIOUaeiou"


def replace_letters(args):
    output = ''
    for i in range(len(args)):
        if args[i].isalpha() and args[i] not in vowels:
            output += random.choice(vowels)
        else:
            output += args[i]
    return output


print(replace_letters(a))
