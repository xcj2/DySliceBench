import sys
from sys import stdin
input = stdin.readline

class BinaryTreeNode:
    def __init__(self, node):
        self.node = node
        self.left = None
        self.right = None

def Insert(parent, child):
    if parent.node > child.node:
        if parent.left != None:
            Insert(parent.left, child)
        else:
            parent.left = child
    else:
        if parent.right != None:
            Insert(parent.right, child)
        else:
            parent.right = child

def Find(root, key):
    if root.node == key:
        print("yes")
    elif root.left == None and key < root.node:
        print("no")
    elif root.right == None and root.node < key:
        print("no")
    else:
        if key < root.node:
            Find(root.left, key)
        else:
            Find(root.right, key)
        

IN_RESULT = []
def Inorder(root):
    if root.left == None:
        IN_RESULT.append(str(root.node))
        if root.right != None:
            Inorder(root.right)
    else:
        Inorder(root.left)
        IN_RESULT.append(str(root.node))
        if root.right != None:
            Inorder(root.right)
        else:
            pass
        
PRE_RESULT = []
def Preorder(root):
    PRE_RESULT.append(str(root.node))
    if root.left != None:
        Preorder(root.left)
    else:
        pass
    
    if root.right != None:
        Preorder(root.right)
    else:
        pass
    
n = int(input())

command = input()
if command[0] == "i":
    root = BinaryTreeNode(int(command[7:]))

for _ in range(n-1):
    command = input()
    if command[0] == "i":
        child = BinaryTreeNode(int(command[7:]))
        Insert(root, child)
    
    elif command[0] == "p":
        Inorder(root)
        Preorder(root)
        print(" "+" ".join(IN_RESULT))
        print(" "+" ".join(PRE_RESULT))
        IN_RESULT = []
        PRE_RESULT = []
    
    else:
        Find(root, int(command[5:]))
