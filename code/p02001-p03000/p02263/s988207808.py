class Stack:
    def __init__(self, size=200):
        self.size = size
        self.data = []
        self.pointer = -1
    
    def push(self, x):
        self.pointer += 1
        self.data.insert(self.pointer, x)
    
    def pop(self):
        ret = self.data[self.pointer]
        self.pointer -= 1
        return ret
    
    def isEmpty(self):
        return len(self.data[:self.pointer + 1]) == 0
    
    def isFull(self):
        return len(self.data) == self.size

def isNumber(s):
    return s.isdigit()

def calc(arg1, arg2, op):
    if (op == '+'):
        return arg1 + arg2
    elif (op == '-'):
        return arg1 - arg2
    elif (op == '*'):
        return arg1 * arg2

IN = input().split()
stack = Stack()
for input_str in IN:
    if isNumber(input_str):
        stack.push(int(input_str))
    else:
        op = input_str
        arg2 = stack.pop()
        arg1 = stack.pop()
        stack.push(calc(arg1, arg2, op))

print(stack.pop())


