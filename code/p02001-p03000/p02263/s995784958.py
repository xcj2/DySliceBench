# Stack

class MyStack:
    def __init__(self):
        self.stack = []
    
    def pop(self):
        return self.stack.pop()
    
    def push(self, x):
        self.stack.append(x)

    def isEmpty(self):
        if len(self.stack)==0:
            return True
        else:
            return False
    
    def isFull(self):
        pass
    
    def calculate(self, x):
        if type(x)==int:
            self.push(x)
        elif type(x)==str:
            b = self.pop()
            a = self.pop()
            if x=='+':
                self.push(a+b)
            elif x=='-':
                self.push(a-b)
            elif x=='*':
                self.push(a*b)


def main():
    A = list(map(lambda x: int(x) if x.isdigit() else x, input().split()))
    stack = MyStack()
    for a in A:
        stack.calculate(a)
    print(stack.pop())

main()
