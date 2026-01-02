class Node:
    def __init__(self, value, prev):
        self.value = value
        self.prev = prev


class Stack:
    def __init__(self):
        self.last = None

    def add(self, value):
        next_node = Node(value, self.last)
        self.last = next_node

    def pop(self):
        if not self.last:
            return -1
        v = self.last.value
        self.last = self.last.prev
        return v


stack = Stack()
s = input().split()
for c in s:
    if c in '+-*':
        a = stack.pop()
        b = stack.pop()
        if c == '+':
            stack.add(a + b)
        elif c == '-':
            stack.add(b - a)
        else:
            stack.add(a * b)
    else:
        stack.add(int(c))

print(stack.pop())

