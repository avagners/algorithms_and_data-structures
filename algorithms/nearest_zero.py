# https://contest.yandex.ru/contest/23390/run-report/66885982/
import sys

"""
Задача: найти расстояние от числа до ближайшего нуля.
Формат ввода:
- в первой строке указано n - кол-во элементов;
- во второй строке n чисел;
Формат вывода:
- расстояние чисел до нуля вывовести в одну строку, разделяя их пробелами

Пример
Ввод:
5
0 1 4 9 0
Вывод
0 1 2 1 0
"""


def zero_dists(start, numbers):
    result = []
    distance = start
    for number in numbers:
        if number == '0':
            distance = 0
        else:
            distance += 1
        result.append(distance)
    return result


def nearest_zero(n, numbers):
    to_left = zero_dists(n, numbers)
    to_right = list(reversed(zero_dists(n, reversed(numbers))))
    return map(min, zip(to_left, to_right))


def read_input():
    count_of_numbers = int(input())
    numbers = sys.stdin.readline().rstrip().split()
    return count_of_numbers, numbers


if __name__ == '__main__':
    count_of_numbers, numbers = read_input()
    print(*nearest_zero(count_of_numbers, numbers))
