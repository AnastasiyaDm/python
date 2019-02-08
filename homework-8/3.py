# Задача -3
# Создать менеджер контекста который будет подсчитывать время выполняния блока инсрукций
import time
from random import randint


class timer:

    def __enter__(self):
        self.start = time.time()
        print("Start time:", self.start)

    def __exit__(self, *exc_info):
        self.diff_time = time.time() - self.start
        print("Execution time:", self.diff_time)


with timer() as f:
    B = list(filter(lambda x: x**2 % 2 == 0, [randint(100, 100000) for x in range(1000, 1000000)]))

