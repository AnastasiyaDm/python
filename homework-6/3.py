# Задача-3 - не обязательна к выполнению
# Написать декоратор который будет подавлять ошибки возникающие в теле вашей функции.
# Например ваша функция может иметь вид
#def my_func():
    #raise ValueError("some text error")


def avoid_err(func):
    def wrapper():
        try:
            func()
        except ValueError as e:
            pass
    return wrapper


@avoid_err
def my_func():
    raise ValueError("some text error")


my_func()
