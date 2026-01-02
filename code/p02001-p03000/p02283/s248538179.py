# coding: utf-8
# Your code here!

class Node:
    def __init__(self,key):
        self.key=key
        self.parent=self.left=self.right=None

def insert(z):
    global root
    x=root
    y=None
    while x:
        y=x
        if z<x.key:
            x=x.left
        else:
            x=x.right
    
    if y==None:
        root=Node(z)
    elif z<y.key:
        y.left=Node(z)
    else:
        y.right=Node(z)

def preorder(x):
    print(" "+str(x.key),end="")
    if x.left != None:
        preorder(x.left)
    if x.right != None:
        preorder(x.right)
        
def inorder(x):
    if x.left != None:
        inorder(x.left)
    print(" "+str(x.key),end="")
    if x.right != None:
        inorder(x.right)
    

root=None

n=int(input())
for i in range(n):
    tmp=input().split()
    if tmp[0]=="insert":
        insert(int(tmp[1]))
    else:
        inorder(root)
        print("")
        preorder(root)
        print("")

