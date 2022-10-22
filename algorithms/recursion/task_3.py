def length(list: list):
    if not list:
        return 0
    list.pop(0)
    return 1 + length(list)
