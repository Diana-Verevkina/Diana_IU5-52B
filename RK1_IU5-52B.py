class hard_drive:
    def __init__(self, id, name, size, id_comp):
        self.id = id
        self.name = name
        self.size = size
        self.id_comp = id_comp

    def get_com_id(self):
        return self.id_comp.id

    def __repr__(self):
        return "Диск: {} комп {}".format(self.name, self.id_comp.name)


class computer:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class UserComputer:
    def __init__(self, id_brow, id_computer):
        self.id_brow = id_brow
        self.id_computer = id_computer


def main():
    comp = [computer(0, 'Apple'),
            computer(1, 'Acer'),
            computer(2, 'Dell'),
            computer(3, 'Huawei'),
            computer(4, 'Asus')
            ]

    brow = [
        hard_drive(0, 'D1', 6, comp[0]),
        hard_drive(1, 'F1', 4, comp[2]),
        hard_drive(2, 'G1', 2, comp[4]),
        hard_drive(3, 'C1', 2, comp[4]),
        hard_drive(4, 'M2', 2, comp[0]),
        hard_drive(5, 'B1', 6, comp[0]),
        hard_drive(6, 'D2', 5, comp[0]),
        hard_drive(7, 'D3', 2, comp[2]),
        hard_drive(8, 'F2', 3, comp[2]),
        hard_drive(9, 'N5', 4, comp[2]),
    ]

    us_comp = [
        UserComputer(0, 0),
        UserComputer(1, 1),
        UserComputer(2, 2),
        UserComputer(2, 3),
        UserComputer(8, 0),
        UserComputer(3, 3),
        UserComputer(4, 3),
        UserComputer(4, 2),
        UserComputer(5, 3),
        UserComputer(6, 1),
        UserComputer(6, 4),
    ]

    print('Задание1')
    res1 = sorted(brow, key=lambda x: x.name.lower())
    print(*res1, sep='\n')

    print('\n\n\nЗадание2')
    l = {}
    for i in range(len(comp)):
        l[i] = 0
    for i in brow:
        l[i.get_com_id()] += 1

    res2 = list(map(lambda x: '{} - кол-ом {}'.format(x.name, l[x.id]), sorted(comp, key=lambda x: l[x.id])))  # сортируем
    print(*res2,sep='\n')


    print('\n\n\nЗадание3')
    l = []
    for i in brow:
        if i.name[-1] == '2':
            for j in us_comp:
                if j.id_brow == i.id:
                    l.append(comp[j.id_computer].name)
            print('Диск: {}, с компами: {}'.format(i.name, l))
            l.clear()


if __name__ == '__main__':
    main()
