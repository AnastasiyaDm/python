# Задача-4
# Изменить исходную строку на новую строку в которой первый и последний символы строки поменяны местами.

s = input('String:')


def update_string(text):
    text = '%s%s%s' % (text[-1], text[1:-1], text[0])
    return text


print(update_string(s))
