def find_second_max(n: list, max_value: int, second_value: int) -> tuple:
    current = n.pop()
    if current >= max_value:
        second_value = max_value
        max_value = current
    elif max_value > current >= second_value:
        second_value = current
    if n:
        max_value, second_value = find_second_max(n, max_value, second_value)
    return max_value, second_value


def main(n: list) -> int:
    number_1, number_2 = n[0], n[1]
    max_value = max(number_1, number_2)
    second_value = min(number_1, number_2)
    max_value, second_value = find_second_max(n, max_value, second_value)
    return second_value
