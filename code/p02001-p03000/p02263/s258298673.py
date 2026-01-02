import sys

class stacker():
    def __init__(self, max):
        self.top = 0
        self.max = max
        self.vlist = list(range(max))
        
    def push(self, x):
        self.top += 1
        self.vlist[self.top] = x
        
    def pop(self):
        self.top -= 1
        return self.vlist[self.top+1]
        
    def isFull(self):
        return self.top == self.max
    
    def isEmpty(self):
        return  self.top == 0
    
def main():

    expr = list(input().split())
    stack = stacker(200)
    for i in expr:
        if i == '+':
            a = stack.pop()
            b = stack.pop()
            stack.push(a+b)
        elif i == '-':
            a = stack.pop()
            b = stack.pop()
            stack.push(b-a)
        elif i == '*':
            a = stack.pop()
            b = stack.pop()
            stack.push(a*b)
        else:
            stack.push(int(i))

    print(stack.vlist[stack.top])
    
            
if __name__ == '__main__':
    main()
