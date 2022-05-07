# https://contest.yandex.ru/contest/24735/run-report/68163605/

def str_to_int(participants):
    participants[1] = - int(participants[1])
    participants[2] = int(participants[2])
    return [participants[1], participants[2], participants[0]]


def effective_quicksort(array, left, right):
    if left >= right:
        return
    pivot = array[left]
    left_index = left
    right_index = right
    while True:
        while array[left_index] < pivot:
            left_index += 1
        while array[right_index] > pivot:
            right_index -= 1
        if left_index <= right_index:
            array[left_index], array[right_index] = array[right_index], array[left_index]
            left_index += 1
            right_index -= 1
        if left_index > right_index:
            break
    effective_quicksort(array, left, right_index)
    effective_quicksort(array, left_index, right)
    return array


def read_input():
    number_of_participants = int(input())
    participants = [
        str_to_int(input().split()) for _ in range(number_of_participants)
        ]
    return participants


if __name__ == '__main__':
    participants = read_input()
    left = 0
    right = len(participants) - 1
    effective_quicksort(participants, left, right)
    print(*(list(zip(*participants))[2]), sep="\n")
