class Stack:

    def __init__(self):
        self.top = 0
        self.stack = [0] * 1000

    def is_empty(self):
        return self.top == 0

    def push(self, x):
        self.top += 1
        self.stack[self.top] = x

    def pop(self):
        if self.is_empty():
            raise RuntimeError
        self.top -= 1
        return self.stack[self.top + 1]


def main():
    A = input().split(' ')
    S = Stack()

    for a in A:

        if a == '+':
            y = S.pop()
            x = S.pop()
            S.push(x + y)
        elif a == '-':
            y = S.pop()
            x = S.pop()
            S.push(x - y)
        elif a == '*':
            y = S.pop()
            x = S.pop()
            S.push(x * y)
        else:
            S.push(int(a))

    print(S.pop())


if __name__ == "__main__":
    main()

