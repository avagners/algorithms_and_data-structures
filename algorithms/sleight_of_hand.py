# https://contest.yandex.ru/contest/23390/run-report/66887675/
"""
Тренажёр представляет собой поле из клавиш 4×4, в котором на каждом раунде
появляется конфигурация цифр и точек. На клавише написана либо точка,
либо цифра от 1 до 9.
В момент времени t игрок должен одновременно нажать на все клавиши,
на которых написана цифра t. 2 игрока могут нажать в один момент времени
на k клавиш каждый. Если в момент времени t были нажаты все нужные клавиши,
то игроки получают 1 балл.

Найдите число баллов, которое смогут заработать 2 игрока,
если будут нажимать на клавиши вдвоём.

Формат ввода
В первой строке дано целое число k (1 ≤ k ≤ 5).
В четырёх следующих строках задан вид тренажёра - 4 символа в каждой строке.
Каждый символ —– либо точка, либо цифра от 1 до 9.
Символы одной строки идут подряд и не разделены пробелами.

Формат вывода
Выведите единственное число –— максимальное количество баллов.
"""
import sys


def sleight_of_hand(keys, output_numbers):
    del_num = set()
    count_num = {}
    max_keys = keys * 2
    for number in output_numbers:
        if number not in del_num:
            if number not in count_num.keys():
                count_num[number] = 1
            else:
                count_num[number] += 1
            if count_num[number] > max_keys:
                del_num.add(number)
                del count_num[number]
    return len(count_num)


def read_input():
    keys = int(input())
    output_numbers = ''
    for _ in range(4):
        line = sys.stdin.readline().rstrip().replace('.', '')
        output_numbers += line
    return keys, output_numbers


if __name__ == '__main__':
    keys, output_numbers = read_input()
    print(sleight_of_hand(keys, output_numbers))
