# Задача-1
# Реализовать дескриптор валидации для аттрибута email.
# Ваш дескриптор должен проверять формат email который вы пытаетесь назначить
import re


class EmailDescriptor:

    def __init__(self, email=None):
        self.email = email

    def __get__(self, instance, owner):
        return self.email

    def __set__(self, instance, new_email):
        if re.match(r"^[_a-zA-Z0-9-]+(\.[_a-zA-Z0-9-]+)?@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)?(\.[a-zA-Z]{2,4})$",
                    new_email):
            self.email = new_email
        else:
            raise ValueError("\'{}\' is not valid email".format(new_email))


class MyClass:
    email = EmailDescriptor()


my_class = MyClass()
my_class.email = "validemail@gmail.com"
print(my_class.email)
# my_class.email = "novalidemail"
# Raised Exception
