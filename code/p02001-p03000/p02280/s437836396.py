class Node:
    def __init__(self):
        self.id = -1
        self.parent = None
        self.childs = [None, None]
        self.sibling = -1
        self.depth = -1
        self.height = -1

    def parentId(self):
        return -1 if self.parent == None else self.parent.id

    def type(self):
        if self.parent == None:
            return "root"
        elif self.childs[0] != None or self.childs[1] != None:
            return "internal node"
        return "leaf"

    def degree(self):
        r = 0
        for c in self.childs:
            r += 1 if c != None else 0
        return r


def setDepthAndHeight(node, d):
    h = 0
    node.depth = d
    for i in range(2):
        if node.childs[i] != None:
            h = max(h, setDepthAndHeight(node.childs[i], d+1)+1)
    node.height = h
    return h


n = int(input())
nodes = [Node() for _ in range(n)]

for i in range(n):
    id, l, r = map(int, input().split())
    p = nodes[id]
    p.id = id
    if l >= 0:
        nodes[l].parent = p
        nodes[l].sibling = r
        p.childs[0] = nodes[l]
    if r >= 0:
        nodes[r].parent = p
        nodes[r].sibling = l
        p.childs[1] = nodes[r]

root = None
for node in nodes:
    if node.type() == "root":
        root = node
        break

setDepthAndHeight(root, 0)

for node in nodes:
    s = f"node {node.id}: "
    s += f"parent = {node.parentId()}, "
    s += f"sibling = {node.sibling}, "
    s += f"degree = {node.degree()}, "
    s += f"depth = {node.depth}, "
    s += f"height = {node.height}, "
    s += f"{node.type()}"
    print(s)

