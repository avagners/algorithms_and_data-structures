def print_even_number(n: list, index=0):
    if index == len(n):
        return
    x = n[index]
    if x % 2 == 0:
        print(x)
    print_even_number(n, index + 1)
