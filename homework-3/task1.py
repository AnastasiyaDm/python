# 1
# Дан произвольный текст. Соберите все заглавные буквы в одно слово в том порядке как они встречаются в тексте.
# Например: текст = "How are you? Eh, ok. Low or Lower? Ohhh.", если мы соберем все заглавные буквы,
# то получим сообщение "HELLO".

text = str(input('Add text: '))


def find_uppercase(t):
    output = ''
    for i in t:
        if i.isupper():
            output = ''.join([output, i])
    return output if output else 'Add another text'


print(find_uppercase(text))
