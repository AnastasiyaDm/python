# 4) Есть массив с положительными числами и число n (def some_function(array, n)).
# Необходимо найти n-ую степень элемента в массиве с индексом n. Если n за границами массива, тогда вернуть -1.


def some_function(array, n):
    return -1 if n > len(array)-1 or n < -len(array) else array[n]**n


input_arr = [1, 5, 6, 8, 9, 2, 0, 0, 1, 2, 3, 10, 1, 5]
x = -5
print(some_function(input_arr, x))







