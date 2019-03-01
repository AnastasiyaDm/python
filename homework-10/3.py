# Задача-3
# Вам нужно создать pipeline (конвеер, подобие pipeline в unix https://en.wikipedia.org/wiki/Pipeline_(Unix)).
#
# Схема пайплайна :
# source --- send()---> coroutine1 ------send()----> coroutine2 ----send()------>sink
#
# Все что вам нужно сделать это выводить сообщение о том что было получено на каждом шаге
# и обработку ошибки GeneratorExit.
#
# Например: Ваш source (это не корутина, не генератор и прочее, это просто функция)
# в ней опеделите цикл из 10 элементов
# которые будут по цепочке отправлены в каждый из корутин и в каждом из корутив вызвано сообщение о полученном элементе.
# После вызова .close() вы должны в каждом из корутин вывести сообщение что работа завершена.


def sink():
    try:
        while True:
            item = (yield)
            print("Receive item \'{}\' from coroutine2 and close".format(item))
    except GeneratorExit:
        print("Exit")


def coroutine2():
    s = sink()
    s.send(None)
    try:
        while True:
            item = (yield)
            print("Send item \'{}\' from coroutine2 to sink".format(item))
            s.send(item)
    except GeneratorExit:
        print("Done with courotine2")
        s.close()


def coroutine1():
    cr2 = coroutine2()
    cr2.send(None)
    try:
        while True:
            item = (yield)
            print("Send item \'{}\' from coroutine1 to coroutine2".format(item))
            cr2.send(item)
    except GeneratorExit:
        print("Done with courotine1")
        cr2.close()


def source(*args):
    cr1 = coroutine1()
    cr1.send(None)
    for item in args:
        print("Send item \'{}\' from source to coroutine1".format(item))
        cr1.send(item)
    cr1.close()


if __name__ == '__main__':
    source(*["1a", "2b", "3c", "4d", "5e", "6f", "7g", "8h", "9i", "10j"])

