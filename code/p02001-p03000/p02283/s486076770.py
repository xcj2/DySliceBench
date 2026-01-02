class Node:
    def __init__(self, key:int):
        self.key = key
        self.p = None
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, z:Node):
        y = None
        x = self.root
        while x != None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y == None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

def Preorder(target:Node):
    yield target.key
    if target.left != None:
        yield from Preorder(target.left)
    if target.right != None:
        yield from Preorder(target.right)

def Inorder(target:Node):
    if target.left != None:
        yield from Inorder(target.left)
    yield target.key
    if target.right != None:
        yield from Inorder(target.right)

from sys import stdin
tree = Tree()
n = int(input())
lines = stdin.readlines()
for line in lines:
    proc,*key = line.split()
    if proc == "insert":
        tree.insert(Node(int(key[0])))
    else:
        print(" ",end="")
        print(*Inorder(tree.root))
        print(" ",end="")
        print(*Preorder(tree.root))
