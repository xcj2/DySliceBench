class MyStack:
    def __init__(self, MAX):
        self.top = 0
        self.stack = [0] * MAX
        self.MAX = MAX
        
    def is_empty(self):
        return self.top <= 0
    
    def is_full(self):
        return self.top >= self.MAX - 1
    
    def push(self, entry):
        if self.is_full():
            raise ValueError()
        self.top += 1
        self.stack[self.top] = entry
    
    def pop(self):
        if self.is_empty():
            raise ValueError()
        self.top -= 1
        return self.stack[self.top + 1]
    
    
stack = MyStack(110)
ope = input().split()

for o in ope:
    if o == '+':
        rh = stack.pop()
        lh = stack.pop()
        stack.push(lh + rh)
        
    elif o == '-':
        rh = stack.pop()
        lh = stack.pop()
        stack.push(lh - rh)
        
    elif o == '*':
        rh = stack.pop()
        lh = stack.pop()
        
        stack.push(lh * rh)
        
    else:
        stack.push(int(o))

result = stack.pop()
print(result)

