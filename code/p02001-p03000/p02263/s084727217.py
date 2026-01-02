top = 0
MAX = 101
S = [0] * MAX


def initialize():
    global top
    top = 0


def isEmpty():
    global top
    return top == 0


def isFull():
    global top
    return top == MAX - 1


def push(a):
    if isFull():
        return
    global top
    top += 1
    S[top] = a


def pop():
    if (isEmpty()):
        return -1
    global top
    top -= 1
    return S[top+1]


def main():
    s = input().split()
    for c in s:
        if c == '+':
            a = pop()
            b = pop()
            push(a + b)
        elif c == '-':
            a = pop()
            b = pop()
            push(b - a)
        elif c == '*':
            a = pop()
            b = pop()
            push(a * b)
        else:
            push(int(c))
    print(pop())


if __name__ == '__main__':
    main()

