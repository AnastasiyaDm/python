# 5) Есть строка со словами и числами, разделенными пробелами (один пробел между словами и/или числами).
# Слова состоят только из букв. Вам нужно проверить есть ли в исходной строке три слова подряд.
# Для примера, в строке "hello 1 one two three 15 world" есть три слова подряд.


def find_words(x, c):
    result = ''
    for i in x.split():
        if i.isalpha():
            result += 'w'
        else:
            result += 'd'
    return True if 'w' * c in result else False


n = 'hello hello 1 one two three 15 world'
count = 3
print(find_words(n, count))



