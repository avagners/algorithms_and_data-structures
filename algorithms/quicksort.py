def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array if i < pivot]
        greater = [i for i in array if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


def read_input():
    list_str = input().split()
    list_num = [int(i) for i in list_str]
    return list_num


if __name__ == '__main__':
    list_num = read_input()
    print(quicksort(list_num))
