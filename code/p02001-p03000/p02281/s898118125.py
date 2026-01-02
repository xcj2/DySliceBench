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


n = int(input())
nodes = [Node() for _ in range(n)]

for i in range(n):
    id, l, r = map(int, input().split())
    p = nodes[id]
    p.id = id
    if l >= 0:
        nodes[l].parent = p
        p.childs[0] = nodes[l]
    if r >= 0:
        nodes[r].parent = p
        p.childs[1] = nodes[r]

root = None
for node in nodes:
    if node.parent == None:
        root = node
        break


def preorder(p):
    s = ""
    if p == None:
        return ""
    s += f"{p.id} "
    s += preorder(p.childs[0])
    s += preorder(p.childs[1])
    return s


def inorder(p):
    s = ""
    if p == None:
        return ""
    s += inorder(p.childs[0])
    s += f"{p.id} "
    s += inorder(p.childs[1])
    return s


def postorder(p):
    s = ""
    if p == None:
        return ""
    s += postorder(p.childs[0])
    s += postorder(p.childs[1])
    s += f"{p.id} "
    return s


print("Preorder")
print(" "+preorder(root).strip())
print("Inorder")
print(" "+inorder(root).strip())
print("Postorder")
print(" "+postorder(root).strip())

