# Задача-2
# У вас несколько JSON файлов. В каждом из этих файлов есть
# произвольная структура данных. Вам необходимо написать
# класс который будет описывать работу с этими файлами, а
# именно:
# 1) Запись в файл
# 2) Чтение из файла
# 3) Объединение данных из файлов в новый файл
# 4) Получить путь относительный путь к файлу
# 5) Получить абсолютный путь к файлу

import json
from pathlib import Path


class MyClass(object):

    def write_to_file(self, testfile, msg):
        with open(testfile, "w") as data_file:
            json.dump(msg, data_file)

    def read_from_file(self, testfile):
        try:
            with open(testfile, "r") as f:
                result = json.load(f)
                return result

        except FileNotFoundError:
            print("File '{}' not found.".format(testfile))

    def merge_files(self, merged, *args):
        result = []
        for f in args:
            result.append(self.read_from_file(f))
        result_to_write = list(filter(lambda x: x is not None, result))
        self.write_to_file(merged, result_to_write)

    def abspath(self, testfile):
        p = Path(testfile).resolve()
        return p


msg = {
        "firstName": "Vanya",
        "lastName": "Sidorov",
        "address": {
            "streetAddress": "Lesnaya str.",
            "city": "Forestwood"
        },
        "phoneNumbers": [
            "222 888888",
            "999 111111"
        ]
    }

testfile1 = 'test/file_to_write1.json'
testfile2 = 'test/file_to_write2.json'
merged = 'test/merged.json'
c = MyClass()
# c.write_to_file(testfile3, msg)
print(c.read_from_file(testfile2))
# c.merge_files(merged, *[testfile1, testfile2, testfile3])
# print(c.abspath(testfile2))
