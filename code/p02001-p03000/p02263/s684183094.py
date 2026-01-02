class Stack:
    def __init__(self, full_idx=10):
        self.stack = [None] * full_idx
        self.top = 0
        self.MAX = full_idx

    def is_empty(self):
        return self.top == 0

    def is_full(self):
        return self.top >= self.MAX - 1

    def push(self, x):
        if self.is_full():
            raise IndexError

        self.top += 1
        self.stack[self.top] = x

    def pop(self):
        if self.is_empty():
            raise IndexError

        self.top -= 1
        return self.stack[self.top+1]


def main():
    e = input().split()
    s = Stack(101)

    for i in range(len(e)):
        if e[i].isdigit():
            s.push(int(e[i]))
        elif e[i] == '+':
            a, b = s.pop(), s.pop()
            s.push(a+b)
        elif e[i] == '-':
            a, b = s.pop(), s.pop()
            s.push(b-a)
        else:
            a, b = s.pop(), s.pop()
            s.push(a*b)

    print(s.pop())


if __name__ == '__main__':
    main()

