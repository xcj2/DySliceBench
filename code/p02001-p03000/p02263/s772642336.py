import sys

ERROR_INPUT = 'input is invalid'
OPECODE = ['+', '-', '*']
STACK = []


def main():
    inp = get_input()
    print(calc_stack(li=inp))


def calc_stack(li):
    if li[0] in OPECODE:
        ans = calc(left=STACK[-2], right=STACK[-1], ope=li[0])

        del li[0]
        if not li:
            return ans

        STACK.pop()
        STACK.pop()
        STACK.append(ans)

        return calc_stack(li=li)

    else:
        STACK.append(int(li[0]))
        del li[0]
        return calc_stack(li=li)


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