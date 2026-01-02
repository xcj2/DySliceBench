class Node:
    def __init__(self,z):
        self.key=z
        self.left=None
        self.right=None

def insert(z):
    global root
    if root==None:
        root=Node(z)
    else:
        x=root
        while True:
            if z<x.key:
                if x.left:
                    x=x.left
                else:
                    x.left=Node(z)
                    break
            else:
                if x.right:
                    x=x.right
                else:
                    x.right=Node(z)
                    break
def inorder(z):
    if z==None:
        return []
    else:
        return inorder(z.left)+[z.key]+inorder(z.right)
def preorder(z):
    if z==None:
        return []
    else:
        return [z.key]+preorder(z.left)+preorder(z.right)
root=None
n=int(input())
for _ in range(n):
    p=input()
    if p[0]=="i":
        insert(int(p[7:]))
    else:
        print("",*inorder(root))
        print("",*preorder(root))
