class Stack:
    def __init__(self, n):
        self.n = n
        self._l = [None for _ in range(self.n + 1)]
        self._top = 0

    def push(self, x):
        if self.isFull():
            raise IndexError("stack is full")
        else:
            self._top += 1
            self._l[self._top] = x

    def pop(self):
        if self.isEmpty():
            raise IndexError("pop from empty stack")
        else:
            e = self._l[self._top]
            self._l[self._top] = None
            self._top -= 1
            return e

    def isEmpty(self):
        return self._top == 0

    def isFull(self):
        return self._top == self.n

def poland_calculator(s):
    n = len(s)
    stack = Stack(n)
    i = 0
    while i < n:
        if s[i] == ' ':
            i += 1
            continue
        elif s[i].isdigit():
            sn = ''
            while s[i].isdigit():
                sn += s[i]
                i += 1
            stack.push(int(sn))
        else:
            b = stack.pop()
            a = stack.pop()
            if s[i] == '+':
                e = a + b
            elif s[i] == '-':
                e = a - b
            else:
                e = a * b
            stack.push(e)
            i +=1

    return stack.pop()


if __name__ == '__main__':
    s = input()
    res = poland_calculator(s)
    print(res)

