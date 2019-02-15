# Задача-3
# реализовать дескриптор IntegerField(), который будет хранить уникальные
# состояния для каждого класса где он объявлен


class IntegerField:

    def __init__(self):
        self.result = {}

    def __get__(self, instance, owner):
        return self.result[instance]

    def __set__(self, instance, value):
        self.result[instance] = value


class Data:
    number = IntegerField()


data_row = Data()
new_data_row = Data()


data_row.number = 5
new_data_row.number = 10


assert data_row.number != new_data_row.number
