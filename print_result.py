def print_result(func):
    def wrapper(*arg):
        print('-----\nИмя оборачиваемой функции: {}'.format(func.__name__))
        print('Результат выполнения:')
        a = func(*arg)#выполняем функцию и сохр результат
        if type(a) == list:#если это список
            print(*a, sep='\n')#выводим в столбик
        elif type(a) == dict:#если это словарь
            for key, value in a.items():
                print("{} = {}".format(key, value))#выводим в столбик в цикле
        else:
            print(a)#иначе просто выводим
        print('-----')
        return a

    return wrapper


@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2, 'c': 3, 'd': 4}


@print_result
def test_4():
    return [1, 2, 'a', 28]


def all_test():
    test_1()
    test_2()
    test_3()
    test_4()
