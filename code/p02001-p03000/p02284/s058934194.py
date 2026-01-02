import sys

class Node:
    def __init__(self,data):
        self.data  = data
        self.left  = None
        self.right = None
    

def insert(node,x):
    if node is None:
        node = Node(x)
    elif node.data == x:
        return node
    elif node.data > x:
        node.left = insert(node.left,x)
    else:
        node.right = insert(node.right,x)
    return node

def search(node,x):
    if node is None:
        return 'no'
    elif node.data == x:
        return 'yes'
    elif node.data > x:
        return search(node.left,x)
    else:
        return search(node.right,x)

class BST:
    def __init__(self):
        self.root = None

    def insert(self,x):
        if self.root is None:
            self.root = Node(x)
        else:
            self.root = insert(self.root,x)
    
    def search(self,x):
        return search(self.root,x)

def mid_walk(node):
    if node is None:
        return 
    yield from mid_walk(node.left)
    yield node.data
    yield from mid_walk(node.right)

def pre_walk(node):
    if node is None:
        return 
    yield node.data
    yield from pre_walk(node.left)
    yield from pre_walk(node.right)


n = int(input())
bt = BST()
for line in sys.stdin:
    if line[0] == 'i':
        bt.insert(int(line[7:]))
    elif line[0] == 'f':
        print(bt.search(int(line[5:])))
    else:
        print(' '+' '.join(map(str,mid_walk(bt.root))))
        print(' '+' '.join(map(str,pre_walk(bt.root))))

