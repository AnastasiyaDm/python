# 2) У вас есть последовательность строк. Необходимо определить наиболее часто встречающуюся строку в последовательности.
# Например:


def most_frequent(list_var):
    return max(list_var, key=list_var.count)


print(most_frequent(['y', 'y', 'bi', 'bi', 'bi']))

