from typing import List


def quicksort(array: list[int]) -> List[int]:
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array if i < pivot]
        greater = [i for i in array if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


def read_input() -> List[int]:
    list_str = input().split()
    list_num = [int(i) for i in list_str]
    return list_num


if __name__ == '__main__':
    numbers: list[int] = read_input()
    print(quicksort(numbers))
