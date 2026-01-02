n = int(input())
nodes = [None] * n
rootIdx = None

class Node:
    parent = property
    node_type = property
    depth = property

    def __init__(self, ID, k, c):
        self.parent = -1
        self.ID = ID
        self.k = k
        self.c = c

    def print_self(self):
        print('node {}: parent = {}, depth = {}, {}, '.format(self.ID, self.parent, self.depth, self.node_type) + str(self.c))

def trace(node, depth):
    node.depth = depth
    if len(node.c) > 0:
        for i in range(len(node.c)):
            child = nodes[node.c[i]]
#            child.parent = node.ID
            trace(child, depth + 1)

for i in range(n):
    s = list(map(int, input().split()))
    ID = s[0]
    k = s[1]
    c = s[2:]
    node = Node(ID, k, c)
    nodes[ID] = node

    # if rootIdx in c:
    #     rootIdx = ID

#print(nodes)
#trace(nodes[0], 0)
for i in range(n):
    node = nodes[i]
    if len(node.c) > 0:
        for i in range(len(node.c)):
            child = nodes[node.c[i]]
            child.parent = node.ID

for i in range(n):
    node = nodes[i]
    if node.parent == -1:
        rootIdx = node.ID

trace(nodes[rootIdx], 0)

for i in range(n):
    node = nodes[i]

    if node.parent == -1:
        node.node_type = 'root'
    elif len(node.c) > 0:
        node.node_type = 'internal node'
    else:
        node.node_type = 'leaf'

for i in range(n):
    nodes[i].print_self()

