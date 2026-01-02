# coding: utf-8
# Your code here!

class Node:
    def __init__(self,key):
        self.key=key
        self.parent=self.left=self.right=None
    

class BST:
    def __init__(self):
        self.root=None
    def insert(self,key):
        node=Node(key)
        insert(self,node)


def insert(t,z):
    x=t.root
    y=None
    while x:
        y=x
        if z.key<x.key:
            x=x.left
        else:
            x=x.right
    z.parent=y
    
    if y==None:
        t.root=z
    elif z.key<y.key:
        y.left=z
    else:
        y.right=z

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

def find(t,k):
    while t:
        if t.key==k:
            return True
        if t.key > k:
            t=t.left
        else:
            t=t.right
    return False



n=int(input())
t=BST()
for i in range(n):
    tmp=input().split()
    if tmp[0]=="insert":
        t.insert(int(tmp[1]))
        
    elif tmp[0]=="find":
        if find(t.root,int(tmp[1])):
            print("yes")
        else:
            print("no")
        
    else:
        inorder(t.root)
        print("")
        preorder(t.root)
        print("")

