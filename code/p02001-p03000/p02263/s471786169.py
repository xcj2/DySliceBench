#Stack
class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

class Stack:
    def __init__(self):
        self.top = None
    
    def push(self,data):
        node = Node(data)
        if self.top==None:
            self.top = node
        else:
            node.next = self.top
            self.top = node
            
    def pop(self):
        if self.top==None:
            return
        else:
            out = self.top
            self.top = self.top.next
            return out

def calc_rpn(x):
    if x=="+" or x=="-" or x=="*":
        a = stack.pop().data
        b = stack.pop().data
        if x=="+":
            stack.push(b + a)
        elif x=="-":
            stack.push(b - a)
        elif x=="*":
            stack.push(b * a)
        
    else:
        stack.push(int(x))

inp = list(input().split())
stack = Stack()

for x in inp:
    calc_rpn(x)
print(stack.pop().data)
