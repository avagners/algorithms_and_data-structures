def find_second_max(n, max_value, second_value):
    current = n.pop()
    if current > max_value:
        second_value = max_value
        max_value = current
    elif max_value > current > second_value:
        second_value = current
    if n:
        max_value, second_value = find_second_max(n, max_value, second_value)
    return max_value, second_value


def main(n):
    number_1, number_2 = n[0], n[1]
    max_value, second_value = ((number_1, number_2) if number_1 >= number_2
                               else (number_2, number_1))
    max_value, second_value = find_second_max(n, max_value, second_value)
    return second_value
