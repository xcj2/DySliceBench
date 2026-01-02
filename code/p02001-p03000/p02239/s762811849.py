class Myqueue():

    def __init__(self, size):
        self.size = size
        self.N = [None for _ in range(size)]
        self.head = 0
        self.tail = 0

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return self.head == (self.tail + 1) % self.size

    def enqueue(self, x):
        if self.is_full():
            raise OverflowError
        self.N[self.tail] = x
        self.tail += 1
        if self.tail == self.size:
            self.tail = 0

    def dequeue(self):
        if self.is_empty():
            raise IndexError
        x = self.N[self.head]
        self.head += 1
        if self.head == self.size:
            self.head = 0
        return x


class Node:

    def __init__(self):
        self.distance = -1
        self.status = 0

    def input_data(self, nodes):
        data = input().split()
        self.number = int(data[0])
        self.v = [nodes[int(x) - 1] for x in data[2:]]

n = int(input())
queue = Myqueue(n)
nodes = [Node() for _ in range(n)]
[node.input_data(nodes) for node in nodes]
nodes[0].status = 1
nodes[0].distance = 0
queue.enqueue(nodes[0])
while not queue.is_empty():
    u = queue.dequeue()
    for v in u.v: #type: Node
        if v.status == 0:
            v.status = 1
            v.distance = u.distance + 1
            queue.enqueue(v)
    u.status = 2


nodes.sort(key=lambda i: i.number)
for node in nodes:
    print(f"{node.number} {node.distance}")
