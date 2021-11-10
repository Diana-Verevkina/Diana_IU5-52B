class Unique(object):
    def __init__(self, items, **kwargs):
        if kwargs.get('ignore_case'):  # если дан флаг
            for i, val in enumerate(items):  # переводим все str в нижний регистр
                if type(val) == str:# если взяли стр
                    items[i] = val.lower()#опускаем текст
        self.items = list(items)

    def __next__(self):
        a = self.l[-1]#сохраняем последний аргумент списка
        while self.n < len(self.items) and self.items[self.n] in self.l:#если мы не прошли весь входной список и данный аргумент  в нашем списке
            self.n += 1#пропускаем его
        if self.n > len(self.items):#если вышли за предел
            raise StopIteration('Достигнут предел итерации')#кидаем ошибку
        elif self.n < len(self.items):#если пока не вышли и не на последнем аргументе
            self.l.append(self.items[self.n])#добавляем не повт. аргумент в наш список
        self.n += 1#берем млед аргумент
        return a#выдаем сохраненный ранее последний аргумент списка

    def __iter__(self):#при созд итератора
        self.l = []#пустой список
        self.n = 1#номер след аргумента для проверки
        self.l.append(self.items[0])#добавляем 0 аргумент, тк его еще не было
        return self
