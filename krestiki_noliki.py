# поле игры
pole_ = list(range(1, 10))

win = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]


# рисую поле
def d_pole_():
    for i in range(3):
        print('|', pole_[0 + i * 3], '|', pole_[1 + i * 3], '|', pole_[2 + i * 3], '|')


def input_(information_):
    while True:
        value = input('Куда ставим ' + information_ + ' ? ')
        # Проверка, что мы вводим число от 1 до 9
        if not (value in '123456789'):
            print('некорректный ввод. Повтор.')
            continue
        # проверк, что поле не занято
        value = int(value)
        if str(pole_[value - 1]) in 'XO':
            print('Тут уже занято')
            continue
        # еслм поле свободно - запись Х или О
        pole_[value - 1] = information_
        break


# проверка на победу
def pobeda_():
    for each in win:
        if (pole_[each[0] - 1]) == (pole_[each[1] - 1]) == (pole_[each[2] - 1]):
            return pole_[each[1] - 1]
    else:
        return False


def L():
    step = 0
    while True:
        d_pole_()
        if step % 2 == 0:
            input_('X')
        else:
            input_('O')
        if step > 3:
            winner = pobeda_()
            if winner:
                d_pole_()
                print(winner, 'победил')
                break
        step += 1
        if step > 8:
            d_pole_()
            print('Ничья')
            break

L()

