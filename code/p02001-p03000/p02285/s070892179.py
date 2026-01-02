#coding:UTF-8
class Node:
    def __init__(self,point):
        self.n=point
        self.left=None
        self.right=None
        
def Insert(t,z):
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

def Find(t,p):
    if t.n == p:
        return True
    elif t.left!=None and t.n>p:
        a=Find(t.left,p)
    elif t.right!=None and t.n<p:
        a=Find(t.right,p)
    else:
        return False
    return a

def Delete(t,p):
    if t.left!=None and t.left.n==p:
        if t.left.left==None and t.left.right==None:
            t.left=None
        elif t.left.left==None and t.left.right!=None:
            t.left=t.left.right
        elif t.left.left!=None and t.left.right==None:
            t.left=t.left.left
        else:
            a=newPoint(t.left.right)
            Delete(t,a)
            t.left.n=a
    elif t.right!=None and t.right.n==p:
        if t.right.left==None and t.right.right==None:
            t.right=None
        elif t.right.left==None and t.right.right!=None:
            t.right=t.right.right
        elif t.right.left!=None and t.right.right==None:
            t.right=t.right.left
        else:
            a=newPoint(t.right.right)
            Delete(t,a)
            t.right.n=a
    else:
        if t.n>p and t.left!=None:
            Delete(t.left,p)
        elif t.n<p and t.right!=None:
            Delete(t.right,p)

def newPoint(t):
    if t.left!=None:
        a=newPoint(t.left)
    else:
        a=t.n
    return a
        

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

def BST3(A,n):
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
            if A[i].split(" ")[0]=="find":
                point=int(A[i].split(" ")[1])
                if Find(tree,point)==True:
                    print("yes")
                else:
                    print("no")
            elif A[i].split(" ")[0]=="delete":
                point=int(A[i].split(" ")[1])
                Delete(tree,point)
            else:    
                z=Node(int(A[i].split(" ")[1]))
                tree=Insert(tree,z)
            
if __name__=="__main__":
    n=int(input())
    A=[]
    for i in range(n):
        A.append(input())
    BST3(A,n)