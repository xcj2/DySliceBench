class Node:
    elm = None
    nxt = None

    def __init__(self, elm, nxt):
        self.elm = elm
        self.nxt = nxt


class MyQueue:
    head = tail = None
    size = 0

    def enqueue(self, x):
        if self.is_empty():
            self.head = self.tail = Node(x, None)
        else:
            self.tail.nxt = Node(x, None)
            self.tail = self.tail.nxt
        self.size += 1

    def dequeue(self):
        n = self.head
        if not self.is_empty():
            self.head = self.head.nxt
            self.size -= 1
        return n.elm

    def is_empty(self):
        return self.size == 0

n, q = map(int, input().split())

s = MyQueue()
result = list()
process = 0

for i in range(n):
    name, time = map(str, input().split())
    s.enqueue([name, int(time)])

while not s.is_empty():

    e = s.dequeue()
    diff = e[1] - q
    if diff <= 0:
        process += e[1]
        result.append([e[0], process])
    else:
        process += q
        s.enqueue([e[0], diff])
for i in result:
    print(i[0], i[1])