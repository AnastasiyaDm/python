# Задача-3
#
# Создайте класс который будет хранить параметры для
# подключения к физическому юниту(например switch). В своем
# списке атрибутов он должен иметь минимальный набор
# (unit_name, mac_address, ip_address, login, password).
# Вы должны описать каждый из этих атрибутов в виде гетеров и
# сеттеров(@property). У вас должна быть возможность
# получения и назначения этих атрибутов в классе.


class MyClass(object):

    def __init__(self):
        self._unit_name = 'unit name'
        self._mac_address = '00:00:00:00:00:00'
        self._ip_address = 'xxx.xxx.xx.xx'
        self._login = 'login'
        self._password = '********'

    @property
    def unit_name(self):
        return self._unit_name

    @property
    def mac_address(self):
        return self._mac_address

    @property
    def ip_address(self):
        return self._ip_address

    @property
    def login(self):
        return self._login

    @property
    def password(self):
        return self._password

    @unit_name.setter
    def unit_name(self, new_unit_name):
        self._unit_name = new_unit_name

    @mac_address.setter
    def mac_address(self, new_mac_address):
        self._mac_address = new_mac_address

    @ip_address.setter
    def ip_address(self, new_ip_address):
        self._ip_address = new_ip_address

    @login.setter
    def login(self, new_login):
        self._login = new_login

    @password.setter
    def password(self, new_password):
        self._password = new_password

    @unit_name.deleter
    def unit_name(self):
        del self._unit_name

    @mac_address.deleter
    def mac_address(self):
        del self._mac_address

    @ip_address.deleter
    def ip_address(self):
        del self._ip_address

    @login.deleter
    def login(self):
        del self._login

    @password.deleter
    def password(self):
        del self._password


c = MyClass()
