def print_even_index(n: list):
    if len(n) == 0:
        return
    print(n[0])
    print_even_index(n[2:])
