# ID 33536647

OPERATORS = '+-*/'
NUMBERS = '1234567890'


def pre_calc(item_a, item_b, oper):
    if oper == '+':
        return item_a + item_b
    elif oper == '-':
        return item_a - item_b
    elif oper == '*':
        return item_a * item_b
    elif oper == '/':
        return int(item_a / item_b)
    raise RuntimeError('Wrong operator')


def calc(array):
    stack = []

    for item in array:
        if item in NUMBERS or len(item) > 1:
            stack.append(item)
        else:
            b, a = stack.pop(), stack.pop()
            interm_res = pre_calc(int(a), int(b), item)
            stack.append(interm_res)
    print(*stack)


data = [x for x in input().split()]
calc(data)
