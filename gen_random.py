from random import randint


def gen_random(n: int, st: int, fin: int):
    l: list = []
    for i in range(n):# n раз выдаем значение рандома
        yield randint(st, fin)
    return l.append(randint(st, fin))