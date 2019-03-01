# Задача-1
# У вас есть файл из нескольких строк. Нужно создать генератор который будет построчно выводить строки из вашего файла.
# При вызове итерировании по генератору необходимо проверять строки на уникальность.
# Если строка уникальна, тогда ее выводим на экран, если нет - скипаем


def my_gen(text_file):
    try:
        with open(text_file, 'r') as f:
            while True:
                res = f.readline()
                if not res:
                    break
                yield res
    except FileNotFoundError:
        print("File '{}' not found.".format(text_file))


my_file = 'test.txt'
unique_lines = []
for line in my_gen(my_file):
    if line not in unique_lines:
        unique_lines.append(line)
        print(line)

