# https://contest.yandex.ru/contest/23759/run-report/67780794/


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            raise IndexError('pop from empty stack')
        return self.items.pop()


OPERATORS = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x // y
}


def read_input():
    input_list = input().split()
    return input_list


def polish_calculator(stack, input_list, operators=OPERATORS):
    for item in input_list:
        if item in operators:
            num1 = stack.pop()
            num2 = stack.pop()
            stack.push(operators[item](num2, num1))
        else:
            stack.push(int(item))
    return stack.pop()


if __name__ == '__main__':
    stack = Stack()
    input_list = read_input()
    result = polish_calculator(stack, input_list)
    print(result)
