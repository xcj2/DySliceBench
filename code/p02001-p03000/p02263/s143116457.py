class Stack:
    def __init__(self):
        self.top = 1
        self.array = [None]*1000

    def push(self, x):
        if not self.isFull():
            self.array[self.top] = x
            self.top += 1
        else:
            raise ValueError()

    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            val = self.array[self.top]
            return val
        else:
            raise ValueError()

    def isEmpty(self):
        if self.top == 1:
            return True
        else:
            return False

    def isFull(self):
        if self.top >= 999:
            return True
        else:
            return False


def main():
    S = input().split()
    stack = Stack()
    operands = ["+", "-", "*"]
    for s in S:
        if s not in operands:
            stack.push(int(s))

        else:
            val1 = stack.pop()
            val2 = stack.pop()
            if s == "+":
                val = val1 + val2
                stack.push(val)
            elif s == "-":
                val = val2 - val1
                stack.push(val)
            else:
                val = val1 * val2
                stack.push(val)
    ans = stack.pop()
    print(ans)


if __name__ == '__main__':
    main()

