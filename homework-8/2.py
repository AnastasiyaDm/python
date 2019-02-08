# Задача -2
# Описать задачу выше но уже с использованием @contexmanager


import os
import contextlib


@contextlib.contextmanager
def cd(path, error, flag):
    try:
        os.chdir(path)
        print(os.getcwd())
    except FileNotFoundError:
        print("No such file or directory")
    try:
        yield {}
    except error:
        if flag:
            pass
        else:
            raise


with cd("/home/user/test", TypeError, False):
    raise TypeError("Исключение TypeError")
