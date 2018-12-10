# 2) У вас есть последовательность строк. Необходимо определить наиболее часто встречающуюся строку в последовательности.
# Например:


def most_frequent(list_var):
    f = {}
    for i in list_var:
        f[i] = list_var.count(i)
    maxim_value = max(f.values())
    for key, value in f.items():
        if value == maxim_value:
            return key


print(most_frequent(['y', 'y', 'bi', 'bi', 'bi']))


