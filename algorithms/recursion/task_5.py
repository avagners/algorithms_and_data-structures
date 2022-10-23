def print_even(n: list):
    '''
    Функция печатает четные числа из списка.
    '''
    if len(n) == 0:
        return
    x = n.pop(0)
    if x % 2 == 0:
        print(x)
    print_even(n)
