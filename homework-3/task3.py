# Задача-3
# Дана строка и нужно найти ее первое слово.
# При решении задачи обратите внимание на следующие моменты:
#   1)В строке могут встречатся точки и запятые
#   2)Строка может начинаться с буквы или, к примеру, с пробела или точки
#   3)В слове может быть апостроф и он является частью слова
#   4)Весь текст может быть представлен только одним словом и все
text = input('String: ')


def find_word(word):
    output = ''
    for i in word:
        if i.isalpha() or i in '\'':
            output = ''.join([output, i])
        elif i.isdigit() or i in ' .,' and not output:
            continue
        else:
            break
    return output

     
print(find_word(text))



