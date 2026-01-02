#coding:utf-8
#1_8_A
class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, node):
        y = None # set parent
        x = self.root
        while x is not None:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right
    
        if y is None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(" {}".format(node.key), end = "")
    inorder(node.right)

def preorder(node):
    if node is None:
        return
    print(" {}".format(node.key), end = "")
    preorder(node.left)
    preorder(node.right)

m = int(input())
t = Tree()
for i in range(m):
    cmd = input().split()
    if cmd[0] == 'insert':
        t.insert(Node(int(cmd[1])))
    else:
        inorder(t.root)
        print()
        preorder(t.root)
        print()