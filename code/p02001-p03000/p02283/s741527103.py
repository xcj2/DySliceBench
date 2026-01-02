import sys
class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

rt = None


def inorder(node):
    return inorder(node.left) + f' {node.data}' + inorder(node.right) if node else ''
def preorder(node):
    return f' {node.data}' + preorder(node.left) + preorder(node.right) if node else ''



def insert(data):
    global rt
    x, y = rt, None
    while x: x, y = x.left if data < x.data else x.right, x
    if y is None: rt = Node(data)
    elif data < y.data: y.left = Node(data)
    else: y.right = Node(data)

n = int(input())
for e in sys.stdin:
    if e[0] == 'i': insert(int(e[7:]))
    else: print(inorder(rt)); print(preorder(rt))

