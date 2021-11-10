import json
from random import randint
from lab_pythone_fp.print_result import print_result
from lab_pythone_fp.cm_timer import cm_timer_1
from lab_pythone_fp.gen_random import gen_random


def start():
    with open('lab_pythone_fp\data_light.json', 'r',
              encoding='utf-8') as f:  # открываем файл personal.json и указываем его кодировку — что бы можно было работать с русскими буквами
        data = json.load(f)  # загоняем в переменную все, что получилось в результате работы библиотеки

        with cm_timer_1():#запускаем последовательность

            print(f4(f3(f2(f1(data)))))
            #f4(f3(f2(f1(data))))


@print_result
def f1(arg):
    return set([x.get("job-name") for x in arg])#возвр список без повторений ключа job-name

@print_result
def f2(arg):
    return list(filter((lambda x: x.split()[0].lower() in 'программист'), arg))#возвр список профессий, который мы делим на слова по пробелу и смотрим, чтобы 1 слово было программист

@print_result
def f3(arg):
    return list(map(lambda x: x + ' с опытом Python', arg))# добавляем ко все мпрофессиям "с опытом Python"

@print_result
def f4(arg):
    #return list(zip(arg, list(map(lambda x: 'с зарплатой ' + x + ' рублей', [str(randint(100000, 200000)) for x in range(len(arg))]))))#проходим по всем профессиям и создаем словари, в которых указываем профессию - рандомную зарплату.Зарплата это список, размером с длину сп. профессий
    return list(zip(arg, list(map(lambda x: 'с зарплатой ' + str(x) + ' рублей', list(gen_random(len(arg),100000,200000 ))))))#проходим по всем профессиям и создаем словари, в которых указываем профессию - рандомную зарплату.Зарплата это список, размером с длину сп. профессий
