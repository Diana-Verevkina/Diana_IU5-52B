from lab_pythone_fp.field import *
from lab_pythone_fp.gen_random import *
from lab_pythone_fp.unique import *
from lab_pythone_fp.sort import *
from lab_pythone_fp.print_result import *
from lab_pythone_fp.cm_timer import *
from lab_pythone_fp.process_data import *


def ex1():
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'color': 'black'},
        {'color': 'wr'},
        {'title': None, 'price': 25, 'color': 'red'},
        {'color': 'blue'},
    ]
    print('Задание 1')
    print(list(field(goods, 'title')))
    print(list(field(goods, 'title', 'price')))


def ex2():
    print('\n\nЗадание 2')
    g = gen_random(5, 1, 3)
    for item in g:
        print(item, end=', ')
    print('\n' , list(gen_random(6, 2, 10)), sep='')


def ex3():
    print('\n\nЗадание 3')
    print('Обработка разного списка')
    data = [1, 1, 1, 1, 1, 2, 2, 2, '2', 2, 2, 'F', 'f', 'A']
    mycl = Unique(data, ignore_case=True)
    myit = iter(mycl)
    while True:
        try:
            print(next(myit))
        except StopIteration:
            break

    print('Обработка генератора')
    mycl1 = Unique(gen_random(10, 1, 3))
    myit1 = iter(mycl1)
    while True:
        try:
            print(next(myit1))
        except StopIteration:
            break


def ex4():
    print('\n\nЗадание 4')
    data = [4, -30, 30, 100, -100, 123, 1, 0, -1, -4]
    srt(data)


def ex5():
    print('\n\nЗадание 5')
    all_test()


def ex6():
    print('\n\nЗадание 6')
    test_cm_timer()


def ex7():
    print('\n\nЗадание 7')
    start()


def main():
    a = (ex1, ex2, ex3, ex4, ex5, ex6, ex7)
    while True:
        print('Выберите задание 1-7:')
        i = int(input())
        if i != 0:
            a[i-1]()
        else:
            return


if __name__ == '__main__':
    main()
