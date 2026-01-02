import sys

sys.setrecursionlimit(10000)

ERROR_INPUT = 'input is invalid'
OPECODE = ['+', '-', '*']
BUF = []


def main():
    stack = get_input()
    ans = calc_stack(stack=stack)
    print(ans)


def calc_stack(stack):
    if stack[-1] in OPECODE:
        BUF.append(stack[-1])
        stack.pop()
        return calc_stack(stack=stack)
    else:
        right_num = int(stack[-1])
        stack.pop()
        if stack[-1] in OPECODE:
            BUF.append(right_num)
            BUF.append(stack[-1])
            stack.pop()
            return calc_stack(stack=stack)
        else:
            left_num = int(stack[-1])
            stack.pop()
            stack.append(calc(left_num, right_num, BUF[-1]))
            BUF.pop()
            stack.extend(reversed(BUF))
            BUF.clear()

        if len(stack) == 1:
            return stack[0]
        else:
            return calc_stack(stack=stack)


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
    OPECODE_count = 0

    for i in inp:
        if i in OPECODE:
            opecode_count += 1
        elif int(i) < 0 or int(i) > 10**6:
            print(ERROR_INPUT)
            sys.exit(1)
        else:
            OPECODE_count += 1

    if opecode_count < 1 or opecode_count > 100:
        print(ERROR_INPUT)
        sys.exit(1)

    if OPECODE_count < 2 or OPECODE_count > 100:
        print(ERROR_INPUT)
        sys.exit(1)

    return inp


main()