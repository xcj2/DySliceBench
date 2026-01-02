n=int(input())
tree={}
root=None

def insert(tree,number):
    parent=None
    children=root
    while children!=None:
        parent=children
        if children>number:
            children=tree[parent][0]
        else:
            children=tree[parent][1]
    
    if parent>number:
        tree[parent][0]=number
    else:
        tree[parent][1]=number

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

def find(x,key):
    while x is not None and key!=x:
        if key<x:x=tree[x][0]
        else:x=tree[x][1]
    return x

for i in range(n):
    tmp=list(input().split())
    if tmp[0]=="print":
        inorder(tree,root)
        print()
        preorder(tree,root)
        print()
    else:
        number=int(tmp[1])
        if tmp[0]=="insert":
            if root is None:
                root=number
                tree[number]=[None,None]
            else:
                tree[number]=[None,None]
                insert(tree,number)
        else:
            if find(root,int(tmp[1])) is not None:print("yes")
            else:print("no")
