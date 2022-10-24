def find_second_max(n, max_value=None, second_max_value=None):
    if max_value is None:
        max_value = n.pop()
    current = n.pop()
    if second_max_value is None and current != max_value:
        second_max_value = current
    if current > max_value:
        second_max_value = max_value
        max_value = current
    elif max_value > current > second_max_value:
        second_max_value = current
    if n:
        return find_second_max(n, max_value, second_max_value)
    return second_max_value
