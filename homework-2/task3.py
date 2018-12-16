# 3) Дано целое число. Необходимо подсчитать произведение всех цифр в этом числе, за исключением нулей.
# Например:
# Дано число 123405. Результат будет: 1*2*3*4*5=120.


def multiply(s):
    if s:
        result = 1
        for i in str(s):
            result *= int(i) if int(i) else 1
    else:
        result = 0
    return result


n = int(input())
print(multiply(n))
