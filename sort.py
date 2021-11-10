def srt(data):
    print('С лямбдой:')
    print(sorted(data, key=lambda x: abs(x), reverse=True))#используем ключ как лямбду
    print('Без лямбды:')
    print(sorted(data, key= abs, reverse=True))  # используем ключ без лямбды
