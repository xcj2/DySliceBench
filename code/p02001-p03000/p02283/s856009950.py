#coding:UTF-8
class Node:
    def __init__(self,point):
        self.n=point
        self.left=None
        self.right=None
        
def insert(t,z):
    y=None
    x=t
    while x!=None:
        y=x
        if z.n<x.n:
            x=x.left
        else:
            x=x.right
    if y==None:
        return z
    else:
        if z.n<y.n:
            y.left=z
        else:
            y.right=z
        return t

def Pre(t,l):
    l.append(str(t.n))
    if t.left!=None:
        Pre(t.left,l)
    if t.right!=None:
        Pre(t.right,l)

def In(t,l):
    if t.left!=None:
        In(t.left,l)
    l.append(str(t.n))
    if t.right!=None:
        In(t.right,l)

def BST1(A,n):
    tree=None
    for i in range(n):
        if A[i]=="print":
            PreAns=[]
            InAns=[]
            Pre(tree,PreAns)
            In(tree,InAns)
            print(" "+" ".join(InAns))
            print(" "+" ".join(PreAns))
        else:
            z=Node(int(A[i].split(" ")[1]))
            tree=insert(tree,z)
            
if __name__=="__main__":
    n=int(input())
    A=[]
    for i in range(n):
        A.append(input())
    BST1(A,n)