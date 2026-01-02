
class Stack:
    def __init__(self, Max=50000):
        self.top = 0
        self.Max = Max
        self.S = []

    def isFull(self):
        return self.top >= self.Max - 1

    def isEmpty(self):
        return self.top == 0

    def push(self, x):
        if self.isFull():
            assert ValueError('max')
        self.top += 1
        self.S.append(x) 

    def pop(self):
        if self.isEmpty():
            assert ValueError('Empty')
        self.top -= 1
        
        return self.S.pop()


formula = list(map(str, input().split()))
S = Stack()

for f in formula:
    # print(S.S)
    if f == '+':
        a = int(S.pop())
        b = int(S.pop())
        S.push(a + b)

    elif f == '-':
        a = int(S.pop())
        b = int(S.pop())
        S.push(b - a)

    elif f == '*':
        a = int(S.pop())
        b = int(S.pop())
        S.push(a * b)
    else:
        S.push(int(f))
        
print(S.pop())

