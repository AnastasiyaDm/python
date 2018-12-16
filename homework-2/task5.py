# 5) Есть строка со словами и числами, разделенными пробелами (один пробел между словами и/или числами).
# Слова состоят только из букв. Вам нужно проверить есть ли в исходной строке три слова подряд.
# Для примера, в строке "hello 1 one two three 15 world" есть три слова подряд.


def find_words(x, c):
    result = []
    string = ''
    for i in x.split():
        result.append('w') if i.isalpha() else result.append('d')
    string = ''.join(result)
    return True if 'w'*c in string else False


n = "hello 1 one two three four five15 world"
count = 3
print(find_words(n, count))



