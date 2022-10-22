def exponentiation(x, y):
    if y == 0:
        return 1
    return x * exponentiation(x, y - 1)
