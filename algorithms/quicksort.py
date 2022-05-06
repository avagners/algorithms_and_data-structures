from typing import List, Tuple
from random import choice


def partition(array, pivot) -> Tuple[List[int], List[int], List[int]]:
    less = [i for i in array if i < pivot]
    center = [i for i in array if i == pivot]
    greater = [i for i in array if i > pivot]
    return less, center, greater


def quicksort(array: list[int]) -> List[int]:
    if len(array) < 2:
        return array
    else:
        pivot = choice(array)
        less, center, greater = partition(array, pivot)
        return quicksort(less) + center + quicksort(greater)


def read_input() -> List[int]:
    list_str = input().split()
    list_num = [int(i) for i in list_str]
    return list_num


if __name__ == '__main__':
    numbers: list[int] = read_input()
    print(quicksort(numbers))
