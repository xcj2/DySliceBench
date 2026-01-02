import sys

ERROR_INPUT = 'input is invalid'
OPECODE = ['+', '-', '*']
STACK = []


def main():
    inp = get_input()
    print(calc_stack(li=inp))


def calc_stack(li):
    for l in li:
        if l in OPECODE:
            STACK.append(calc(right=STACK.pop(), left=STACK.pop(), ope=l))
        else:
            STACK.append(int(l))

    return STACK[0]


def calc(left, right, ope):
    if ope == '+':
        return left + right
    elif ope == '-':
        return left - right
    elif ope == '*':
        return left * right


def get_input():
    inp = input().split(' ')
    opecode_count = 0
    operand_count = 0

    for i in inp:
        if i in OPECODE:
            opecode_count += 1
        elif int(i) < 0 or int(i) > 10**6:
            print(ERROR_INPUT)
            sys.exit(1)
        else:
            operand_count += 1

    if opecode_count < 1 or opecode_count > 100:
        print(ERROR_INPUT)
        sys.exit(1)

    if operand_count < 2 or operand_count > 100:
        print(ERROR_INPUT)
        sys.exit(1)

    return inp


main()