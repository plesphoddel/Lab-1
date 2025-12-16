#ПЛЕСКАЧЁВА, ВАРИАНТ 3, ИСУ 502603

import time, sys

RED = '\u001b[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
BLACK = '\u001b[40m'
END = '\u001b[0m'
ERASE = '\x1B[2K' # erase the line
BEGIN = '\x1B[1G' # return to column 1

#ЗАДАНИЕ 1 - ФЛАГ НИДЕРЛАНДОВ
def flag():
    line = ' ' * 4
    lenght = 15
    height = lenght
    for i in range(1, height + 1):
        if i < 6:
            print(f'{RED}{line * lenght}{END}')
        elif i < 11:
            print(f'{WHITE}{line * lenght}{END}')
        else:
            print(f'{BLUE}{line * lenght}{END}')

#ЗАДАНИЕ 2 - ФЛАГ НИДЕРЛАНДОВ
def pattern():
    line = ' ' * 2
    lenght = 9
    height = lenght
    for i in range(1, height + 1):
        if i < (lenght + 1) // 2:
            print(f'{WHITE}{(i - 1)*line}{BLACK}{line}{WHITE}{(lenght - i * 2)*line}{BLACK}{line}{WHITE}{(i - 1)*line}{END}', end = '')
            print(f'{WHITE}{(i - 1)*line}{BLACK}{line}{WHITE}{(lenght - i * 2)*line}{BLACK}{line}{WHITE}{(i - 1)*line}{END}')
        elif i == (lenght + 1) // 2:
            print(f'{WHITE}{(lenght // 2)*line}{BLACK}{line}{WHITE}{(lenght // 2)*line}{END}', end = '')
            print(f'{WHITE}{(lenght // 2)*line}{BLACK}{line}{WHITE}{(lenght // 2)*line}{END}')
        else:
            print(f'{WHITE}{(lenght - i)*line}{BLACK}{line}{WHITE}{(lenght - (lenght - i + 1) * 2)*line}{BLACK}{line}{WHITE}{(lenght - i)*line}{END}', end = '')
            print(f'{WHITE}{(lenght - i)*line}{BLACK}{line}{WHITE}{(lenght - (lenght - i + 1) * 2)*line}{BLACK}{line}{WHITE}{(lenght - i)*line}{END}')

#ЗАДАНИЕ 3 - ГРАФИК(y = 2x)
def function():
    print("График y = 2x")
    print("  ^")
    for y in range(20, 1, -2):
        print(f"{y:2.0f}|{' ' * (y // 2 - 1)}*")
    print("  *------------------>")
    print("   12345678910")


#ЗАДАНИЕ 4
def diagrama():
    file = open('sequence.txt', 'r')
    list = []
    for _ in file:
        list.append(float(_))
    file.close()

    even_numbers = 0
    odd_numbers = 0
    for i in range(len(list)): #так как индексы идут с 0, то нечетные числа будут на местах с чётными индексами
        if i % 2 == 0:
            odd_numbers += abs(list[i])
        else:
            even_numbers += abs(list[i])
    print(f"Сумма модулей чисел на чётных позициях  = {even_numbers:.2f}")
    print(f"Сумма модулей чисел на нечётных позициях = {odd_numbers:.2f}")
    even_percent = even_numbers * 100.0 / (even_numbers + odd_numbers)
    odd_percent = odd_numbers * 100.0 / (even_numbers + odd_numbers)
    length = 1
    print("Диаграмма процентного соотношения суммы модулей чисел:")
    print(f'Чётные   {even_percent:.2f}% {RED}{" " * int(even_percent * length)}{END}')
    print(f'Нечётные {odd_percent:.2f}% {BLUE}{" " * int(odd_percent * length)}{END}')


#ЗАДАНИЕ 5 - ДОПОЛНИТЕЛЬНОЕ
import os
import time

def px(color, length=2): #рисуем 1 пиксель цветом и сбрасываем цвет
    return (f'\x1b[48;5;{color}m' + (' ' * length) + '\x1b[0m')

def draw_row(row, color, offset=2, length=2): #рисуем 1 строку буквы, row_mask- массив, описывающий строку
    s = ' ' * offset #отступ
    for v in row: #перебираем значения в массиве строки, если 1, печатаем цветной пиксель
        s += px(color, length=2) if v else (' ' * length)
    print(s)

def draw(massive, color, offset=2, length=2): #перебираем все строки в массиве и печатаем 1 букву
    for row in massive:
        draw_row(row, color, offset, length)

G = [
    [1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,0,0,0,0,0,0,0,0,0,0],
    [1,1,0,0,0,0,0,0,0,0,0,0],
    [1,1,0,0,0,0,0,0,0,0,0,0],
    [1,1,0,0,0,0,0,0,0,0,0,0],
    [1,1,0,0,0,0,0,0,0,0,0,0],
    [1,1,0,0,0,0,0,0,0,0,0,0],
    [1,1,0,0,0,0,0,0,0,0,0,0]]

U = [ 
    [1,1,0,0,0,0,0,0,0,0,1,1],
    [1,1,0,0,0,0,0,0,0,0,1,1],
    [1,1,0,0,0,0,0,0,0,0,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,0,1,1],
    [0,0,0,0,0,0,0,0,0,0,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1]]

D = [ 
    [0,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,0,0,0,0,0,0,1,1,0],
    [0,1,1,0,0,0,0,0,0,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,0],
    [1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,0,0,0,0,0,0,0,0,1,1],
    [1,1,0,0,0,0,0,0,0,0,1,1],
    [1,1,0,0,0,0,0,0,0,0,1,1]]

def animate():
    colors = [13, 1, 21]
    alf = [G, U, D]
    k = 0
    while k < 3:
        os.system("cls")
        draw(alf[k], colors[k])
        k = (k + 1) % 3
        time.sleep(1)

#ОТВЕТЫ
#flag()
#pattern()
#function()
#diagrama()
#animate()