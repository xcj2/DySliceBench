class Heap():
    def __init__(self, H):
        self.n = len(H)
        self.nodes = {}
        for i, key in enumerate(H):
            self.add_node(i+1, key)
        self.connect()

    def add_node(self, index, key):
        if index not in self.nodes:
            self.nodes[index] = Node(index, key)

    def connect(self):
        for i in range(1, self.n+1):
            if i//2 != 0:
                self.nodes[i].parent = self.nodes[i//2]
            if i*2 <= self.n:
                self.nodes[i].left = self.nodes[i*2]
            if i*2+1 <= self.n:
                self.nodes[i].right = self.nodes[i*2 + 1]


class Node():
    def __init__(self, index, key):
        self.index = index
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

    def __str__(self):
        out = 'node {}: key = {}, '.format(self.index, self.key)
        if self.parent:
            out += 'parent key = {}, '.format(self.parent.key)
        if self.left:
            out += 'left key = {}, '.format(self.left.key)
        if self.right:
            out += 'right key = {}, '.format(self.right.key)
        return out


n = int(input())
H = list(map(int, input().split()))
heap = Heap(H)
for i in range(1, n+1):
    print(heap.nodes[i])

