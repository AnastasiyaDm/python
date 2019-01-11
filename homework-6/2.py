# Задача-2
# Текстовый файл содержит записи о телефонах и их владельцах.
# Переписать в другой файл телефоны тех владельцев, фамилии которых начинаются с букв К и С.


def rewrite(file_to_read, file_to_write):
    with open(file_to_write, 'w') as res:
        with open(file_to_read, 'r') as file:
            for line in file:
                owner = line.split()
                if owner[0].startswith(('K', 'C')):
                    res.write(owner[1] + '\n')


rewrite('phones.txt', 'result.txt')