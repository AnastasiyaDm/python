# Задача-2
# представим есть файл с логами, его нужно бессконечно контролировать
# на предмет возникнования заданных сигнатур.
#
# Необходимо реализовать пайплайн из корутин, который подключается к существующему файлу
# по принципу команды tail, переключается в самый конец файла и с этого момента начинает следить
# за его наполнением, и в случае возникнования запиcей, сигнатуры которых мы отслеживаем -
# печатать результат
#
# Архитектура пайплайна

#                    --------
#                   /- grep -\
# dispenser(file) <- - grep - -> pprint
#                   \- grep -/
#                    --------

# Структура пайплайна:
"""
def coroutine(*args):
    # your code here


@coroutine
def grep(*args):
    # your code here


@coroutine
def printer():
    # your code here


@coroutine
def dispenser(*args):
    # your code here


def follow(*args):
    # your code here
"""
# Каждый grep следит за определенной сигнатурой
# Как это будет работать:

""" 
f_open = open('log.txt') # подключаемся к файлу
follow(f_open,
       # делегируем ивенты
       dispenser([
           grep('python', printer()), # отслеживаем
           grep('is', printer()),     # заданные
           grep('great', printer()),  # сигнатуры
       ])) 
"""
# Как только в файл запишется что-то содержащее ('python', 'is', 'great') мы сможем это увидеть
# Итоговая реализация фактически будет асинхронным ивент хендлером, с отсутствием блокирующих операций.
import functools
import os
import time


def coroutine(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        c = func(*args, **kwargs)
        next(c)
        return c
    return wrapper


@coroutine
def grep(pattern, my_func):
    while True:
        line = (yield)
        if pattern in line:
            my_func.send(line)



@coroutine
def printer():
    while True:
        line = (yield)
        print(line)


@coroutine
def dispenser(*args):
    while True:
        item = (yield)
        for my_func in args:
            my_func.send(item)


def follow(input_file, my_func):
    input_file.seek(0, os.SEEK_END)
    while True:
        line = input_file.readline()
        if not line:
            time.sleep(0.1)
            continue
        my_func.send(line)
    my_func.close()


def main():
    try:
        text_file = open('test.txt', 'r')
    except FileNotFoundError:
        print('No input file')
    follow(text_file, dispenser(*[grep('python', printer()), grep('we', printer()), grep('cat', printer())]))


if __name__ == '__main__':
    main()
