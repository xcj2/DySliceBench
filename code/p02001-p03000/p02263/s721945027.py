import sys
input = sys.stdin.readline


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.parent = None


class Stack:
    def __init__(self):
        self.head = Node(None)
        self.top = self.head

    def push(self, node: Node):
        if self.top == self.head:
            self.head.next = node
            node.parent = self.head
            self.top = node
        else:
            self.top.next = node
            node.parent = self.top
            self.top = node

    def pop(self):
        if self.top == self.head:
            return None
        else:
            _tmp = self.top
            self.top = self.top.parent
            self.top.next = None
            return _tmp


ops = input().strip().split()

stack = Stack()

for op in ops:
    if op == "+":
        _a = stack.pop().val
        _b = stack.pop().val
        stack.push(Node(_a + _b))
    elif op == "-":
        _a = stack.pop().val
        _b = stack.pop().val
        stack.push(Node(_b - _a))
    elif op == "*":
        _a = stack.pop().val
        _b = stack.pop().val
        stack.push(Node(_a * _b))
    else:
        stack.push(Node(int(op)))

print(stack.pop().val)

