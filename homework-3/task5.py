# Задача-5
# Дан тапл(tuple), необходимо его конвертнуть в стринг.
# Например:
# ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's') == 'exercises


t = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')


def convert(res):
    output = ''
    for i in res:
        output = ''.join([output, str(i)])
    return output


print(convert(t))
