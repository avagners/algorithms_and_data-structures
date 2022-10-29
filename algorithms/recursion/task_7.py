from typing import List, Tuple
from random import choice


def partition(array, pivot) -> Tuple[List[int], List[int], List[int]]:
    less = [i for i in array if i < pivot]
    center = [i for i in array if i == pivot]
    greater = [i for i in array if i > pivot]
    return less, center, greater


def quicksort(array: List[int]) -> List[int]:
    if len(array) < 2:
        return array
    pivot = choice(array)
    less, center, greater = partition(array, pivot)
    return quicksort(less) + center + quicksort(greater)


def find_second_max_value(n: list) -> int:
    sorted_numbers = quicksort(n)
    second_value = sorted_numbers[-2]
    return second_value
