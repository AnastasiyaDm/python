# Задача-4 - не обязательна к выполнению
# Написать декоратор c аргументом который будет подавлять определенные ошибки возникающие в теле вашей функции.
# Ошибки которые должен будет подавить ваш декоратор вы должны передать ему в качестве аргумента


def main_decorator(*args):
    def avoid_err(func):
        def wrapper():
            try:
                func()
            except Exception as e:
                if isinstance(e, args):
                    pass
                else:
                    print(e)
        return wrapper
    return avoid_err


errors = [ValueError, NameError, TypeError]


@main_decorator(*errors)
def my_func():
    raise NameError('Error!!!')


my_func()
