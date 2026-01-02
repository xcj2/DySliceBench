class Stack:

    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        ans = self.stack[-1]
        del self.stack[-1]
        return ans

    def IsEmpty(self):
        return len(self.stack) == 0

def Reverse_polish(lst):
    stack = Stack()
    for i in range(len(lst)):
        if lst[i] == "+":
            a = stack.pop()
            b = stack.pop()
            stack.push(a + b)
        elif lst[i] == "-":
            a = stack.pop()
            b = stack.pop()
            stack.push(b - a)
        elif lst[i] == "*":
            a = stack.pop()
            b = stack.pop()
            stack.push(a * b)
        elif lst[i] == "/" and stack.stack[-1] != 0:
            a = stack.pop()
            b = stack.pop()
            stack.push(b / a)
        else:
            stack.push(int(lst[i]))
    print(stack.stack[-1])

lst = list(map(str, input().split()))
Reverse_polish(lst)        
            
