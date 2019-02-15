# Задача-2
# Реализовать синглтон метакласс(класс для создания классов синглтонов).


class Singleton(type):

    instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.instances:
            cls.instances[cls] = super().__call__(*args, **kwargs)
        return cls.instances[cls]


class MyClass(metaclass=Singleton):
    pass


c = MyClass()
b = MyClass()
assert id(c) == id(b)
