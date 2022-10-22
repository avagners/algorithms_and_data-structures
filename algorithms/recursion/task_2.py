def sum_number(n):
    if n < 10:
        return n
    return n % 10 + sum_number(n // 10)
