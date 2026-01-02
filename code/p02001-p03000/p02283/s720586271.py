n=int(input())

tree={}
root=None

def insert(tree,number):
    y=None
    x=root
    while x!=None:
        y=x
        if number<x:
            x=tree[y][0]
        else:
            x=tree[y][1]

    if number<y:
        tree[y][0]=number
    else:
        tree[y][1]=number

def preorder(tree,i):
    if i==None:
        return
    print(" {}".format(str(i)),end="")
    preorder(tree,tree[i][0])
    preorder(tree,tree[i][1])

def inorder(tree,i):
    if i==None:
        return
    inorder(tree,tree[i][0])
    print(" {}".format(str(i)),end="")
    inorder(tree,tree[i][1])

for i in range(n):
    tmp=list(input().split())
    if tmp[0]=="insert":
        number=int(tmp[1])
        if root==None:
            root=number
            tree[root]=[None,None]
        else:
            tree[number]=[None,None]
            insert(tree,number)
    
    else:
        inorder(tree,root)
        print()
        preorder(tree,root)
        print()
