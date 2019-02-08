# Создать объект менеджера контекста который будет переходить
# в папку которую он принимает на вход.
# Так же ваш объект должен принимать исключение которое он будет подавлять.
# Если флаг об исключении отсутствует, исключение должно быть поднято.
#
import os


class cd:

    def __init__(self, path, error, flag):
        self.path = path
        self.errors = error
        self.flag = flag

    def __enter__(self):
        self.saved_cwd = os.getcwd()
        try:
            os.chdir(self.path)
            print("You change dir from \'{}\' to \'{}\'".format(self.saved_cwd, os.getcwd()))
        except FileNotFoundError:
            print("No such file or directory")

    def __exit__(self, type, value, trace):
        if type is not None and issubclass(type, self.errors):
            return self.flag


with cd("/home/user/test", TypeError, False) as f:
    raise TypeError("Исключение TypeError")
