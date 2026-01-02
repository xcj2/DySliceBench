import sys

class Node:
    def __init__(self,data=None):
        self.data  = data
        self.left  = None
        self.right = None
    
def search(node,x):
    if node is None:
        return 'no'
    elif node.data == x:
        return 'yes'
    elif node.data > x:
        return search(node.left,x)
    else:
        return search(node.right,x)

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

def search_min(node):
    if node.left is None:
        return node.data
    return search_min(node.left)

def delete_min(node):
    if node.left is None:
        return node.right
    node.left = delete_min(node.left)
    return node

def delete(node,x):
    if node:
        if x == node.data:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                node.data = search_min(node.right)
                node.right = delete_min(node.right)
        elif x < node.data:
            node.left = delete(node.left,x)
        else:
            node.right = delete(node.right,x)
    return node

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

    def delete(self,x):
        self.root = delete(self.root,x)

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
    if line[:1] == 'i':
        bt.insert(int(line[7:]))
    elif line[:1] == 'f':
        print(bt.search(int(line[5:])))
    elif line[:1] == 'p':
        print(' '+' '.join(map(str,mid_walk(bt.root))))
        print(' '+' '.join(map(str,pre_walk(bt.root))))
    else:
        bt.delete(int(line[7:]))



