def print_even_index(n: list, index=0):
    if index % 2 == 0:
        print(n[index])
    if index == len(n) - 1:
        return
    print_even_index(n, index + 1)
    