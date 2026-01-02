import sys

class Node:
    __slots__ = ['key', 'left', 'right']
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    def insert(self, key):
        x = self.root
        y = None
        z = Node(key)
        while x != None:
            y = x
            x = x.left if z.key < x.key else x.right
        if y == None: self.root = z
        else:
            if z.key < y.key: y.left = z
            else: y.right = z
    def print_tree(self):
        def inorder(node):
            return inorder(node.left) + f' {node.key}' + inorder(node.right) if node else ''
        def preorder(node):
            return f' {node.key}' + preorder(node.left) + preorder(node.right) if node else ''
        print(inorder(self.root))
        print(preorder(self.root))

tree = BST()
input()
for e in sys.stdin:
    if e[0] == 'i': tree.insert(int(e[7:]))
    else: tree.print_tree()
