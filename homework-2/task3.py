# 3) Дано целое число. Необходимо подсчитать произведение всех цифр в этом числе, за исключением нулей.
# Например:
# Дано число 123405. Результат будет: 1*2*3*4*5=120.


def multiply(s):
    if s != 0:
        result = 1
        for i in str(s):
            if i != '0':
                result *= int(i)
    else:
        result = 0
    return result


n = int(input())
print(multiply(n))
