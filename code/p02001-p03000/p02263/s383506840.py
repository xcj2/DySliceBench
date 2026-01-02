def is_operator(op):
    if '+' == op:
        return True
    if '-' == op:
        return True
    if '*' == op:
        return True

    return False

def operate(op, stack):
    if not is_operator(op):
        stack.append(op)
        return stack

    n2 = int(stack.pop())
    n1 = int(stack.pop())

    if '+' == op:
        n = n1+n2
    if '-' == op:
        n = n1-n2
    if '*' == op:
        n = n1*n2

    stack.append(str(n))

    return stack

def main():
    ops = input().split()

    stack = []
    for op in ops:
        stack = operate(op, stack)

    print(stack.pop())

if __name__ == '__main__':
    main()

