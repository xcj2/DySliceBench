def is_float_str(num_str, default=0):
    try:
        return {"is_float": True, "val": float(num_str)}
    except ValueError:
        return {"is_float": False, "val": default}


def compute(operand, val1, val2):
    if operand == "+":
        return val2 + val1
    elif operand == "-":
        return val2 - val1
    elif operand == "*":
        return val2 * val1
    elif operand == "/":
        return val2 / val1


def get_input():
    while True:
        try:
            yield input()
        except EOFError:
            break


if __name__ == '__main__':
    # split with ' '
    formulas = list(get_input())
    for (i, formula) in enumerate(formulas, 0):
        formulas[i] = formula.split(' ')
    stack = []

    for formula in formulas:
        stack = []
        for elm in formula:
            if is_float_str(elm)["is_float"]:
                stack.append(is_float_str(elm)["val"])
            elif elm in ['+', '-', '*', '/']:
                stack.append(compute(elm, stack.pop(), stack.pop()))
        if len(stack) == 1:
            print(format(stack[0], '.6f'))

