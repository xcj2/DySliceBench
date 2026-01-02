import sys

class Stack:
    def __init__(self, max):
        self.max = max
        self.stack = list(range(max))
        self.top = 0

    def push(self, value):
        if self.top == self.max:
            raise IndexError('?????????????????????????????????')

        self.stack[self.top] = value
        self.top += 1

    def pop(self):
        if self.top == 0:
            raise IndexError('??????????????????????????¨??????')

        self.top -= 1
        return self.stack[self.top]

def main():
    expr = sys.stdin.readline().strip().split(' ')
    stack = Stack(100)
    
    for i in expr:
        if i == '*' or i == '+' or i == '-':
            n1 = stack.pop()
            n2 = stack.pop()
            ans = eval(n2 + i + n1)
            stack.push(str(ans))
        else:
            stack.push(i)

    print(stack.pop())
    
if __name__ == '__main__':
    main()