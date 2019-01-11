# Задача-1
# Из текстового файла удалить все слова, содержащие от трех до пяти символов,
# но при этом из каждой строки должно быть удалено только четное количество таких слов.


def delete_words(filename):
    with open(filename, 'r') as file:
        data = file.readlines()

    with open(filename, 'w') as res:
        for s in data:
            string = s.split()
            words_to_delete = list(filter(lambda word: 3 <= len(word) <= 5, string))
            if len(words_to_delete) % 2 == 0:
                words_to_write = list(filter(lambda word: word not in words_to_delete, string))
                res.write(' '.join(words_to_write) + '\n')
            else:
                words_to_write = list(filter(lambda word: word not in words_to_delete[:-1], string))
                res.write(' '.join(words_to_write) + '\n')


delete_words('test.txt')
