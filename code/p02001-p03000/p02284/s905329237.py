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

def find(node, k):
    while node:
        if node.data == k:
            return True
        if k < node.data:
            node = node.left
        else:
            node = node.right
    return False

def insert(data):
    global rt
    x, y = rt, None
    while x: x, y = x.left if data < x.data else x.right, x
    if y is None: rt = Node(data)
    elif data < y.data: y.left = Node(data)
    else: y.right = Node(data)

n = int(input())
b = [input() for i in range(n)]
for e in b:
    if e[0] == 'i': insert(int(e[7:]))
    elif e[0] =='f':
        if find(rt,int(e[5:])):
            print('yes')
        else:
            print('no')
    else:
        print(inorder(rt))
        print(preorder(rt))


