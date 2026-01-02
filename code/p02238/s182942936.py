class Node:

    def __init__(self):
        self.distime = 0
        self.fintime = 0

    def input_data(self, nodes):
        data = input().split()
        self.number = int(data[0])
        self.v = [nodes[int(x) - 1] for x in data[2:]]

    @property
    def status(self):
        return bool(self.distime) + bool(self.fintime)

class Stack:
    def __init__(self, size):
        self.size = size
        self.N = [None for _ in range(size)]
        self.top = 0

    def is_emtpy(self):
        return self.top == 0

    def is_full(self):
        return self.top == self.size

    def front(self):
        return self.N[self.top - 1]

    def push(self, x):
        if self.is_full():
            raise OverflowError
        self.N[self.top] = x
        self.top += 1

    def pop(self):
        if self.is_emtpy():
            raise IndexError
        self.top -= 1
        return self.N[self.top]


def visit(node: Node):
    global t
    stack.push(node)
    t += 1
    node.distime = t
    while not stack.is_emtpy():
        u: Node = stack.front()
        try:
            v = next(i for i in u.v if i.status == 0)
        except StopIteration:
            stack.pop()
            t += 1
            u.fintime = t
        else:
            if v.status == 0:
                stack.push(v)
                t += 1
                v.distime = t


n = int(input())
stack = Stack(n)
nodes = [Node() for _ in range(n)]
[node.input_data(nodes) for node in nodes]
t = 0
for node in nodes:
    if node.status == 0:
        visit(node)

nodes.sort(key=lambda i: i.number)
for node in nodes:
    print(f"{node.number} {node.distime} {node.fintime}")
