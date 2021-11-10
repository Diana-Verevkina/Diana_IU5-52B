import time
from contextlib import contextmanager


class cm_timer_1:
    def __enter__(self):#запуск
        self.start_time = time.time()#сохр время

    def __exit__(self, exc_type, exc_val, exc_tb):#выход
        print("Время выполнения {} секунд".format(time.time() - self.start_time))#выводим время
        if exc_val:# если получили экз иисключ
            raise


@contextmanager
def cm_timer_2():
    start_time = time.time()#запуск
    yield
    print("Время выполнения {} секунд".format(time.time() - start_time))#выход


def test_cm_timer():
    print('Вызываем конт. мен. как класс')
    with cm_timer_1():
        time.sleep(1)

    print('Вызываем конт. мен. как contextmanager')
    with cm_timer_2():
        time.sleep(1)
