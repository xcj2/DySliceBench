class MyStack:
    def __init__(self, size):
        self.stack = [0 for i in range(size)]
        self.size = size
        self.top = 0

    def initialize(self):
        self.top = 0

    def push(self, elm):
        self.top += 1
        self.stack[self.top] = elm
        return self.stack

    def pop(self):
        ret = self.stack[self.top]
        self.stack[self.top] = 0
        self.top -= 1
        return ret

    def is_empth(self):
        if not self.is_full():
            return True
        return False

    def is_full(self):
        if self.size-1 is self.top:
            return True
        return False


def main(expr):
    stack = MyStack(1000)
    for i, elm in enumerate(expr):
        if expr[i] is '+':
            a = stack.pop()
            b = stack.pop()
            stack.push(int(a) + int(b))
        elif expr[i] is '-':
            a = stack.pop()
            b = stack.pop()
            stack.push(int(b) - int(a))
        elif expr[i] is '*':
            a = stack.pop()
            b = stack.pop()
            stack.push(int(a) * int(b))
        else:
            stack.push(elm)
    return stack.pop()


if __name__ == '__main__':
    expr = [str(s) for s in input().split()]
    print(main(expr))