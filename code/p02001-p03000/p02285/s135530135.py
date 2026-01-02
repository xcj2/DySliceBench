n=int(input())
tree={}
root=None

def insert(tree,number):
    parent=None
    children=root
    while children!=None:
        parent=children
        if number>children:
            children=tree[parent][1]
        else:
            children=tree[parent][0]
    tree[number][2]=parent
    if number>parent:
        tree[parent][1]=number
    else:
        tree[parent][0]=number

def preorder(tree,i):
    if i==None:
        return
    print(" {}".format(i),end="")
    preorder(tree,tree[i][0])
    preorder(tree,tree[i][1])

def inorder(tree,i):
    if i==None:
        return
    inorder(tree,tree[i][0])
    print(" {}".format(i),end="")
    inorder(tree,tree[i][1])

def find(x,number):
    while x!=None and number!=x:
        if x>number:
            x=tree[x][0]
        else:
            x=tree[x][1]
    return x

def find_parent(x,number):
    y=0
    t=-1
    while x!=None and number!=x:
        y=x
        if x>number:
            x=tree[x][0]
            t=0
        else:
            x=tree[x][1]
            t=1
    return y,t

def get_minimum(tree,number):
    while tree[number][0]!=None:
        number=tree[number][0]
    return number    

def delete(tree,number):
    if tree[number][0]==None and tree[number][1]==None:
        y,t=find_parent(root,number)
        tree[y][t]=None
    elif tree[number][0]==None or tree[number][1]==None:
        if tree[number][0]==None:
            next_number=tree[number][1]
        else:
            next_number=tree[number][0]
        y,t=find_parent(root,number)
        tree[y][t]=next_number
    elif tree[number][0]!=None and tree[number][1]!=None:
        next_number=get_minimum(tree,tree[number][1])
        y,t=find_parent(root,number)
        next_y,next_t=find_parent(root,next_number)
        left,right=tree[number][0],tree[number][1]
        if tree[number][1]==next_number:
            right=None
        tree[y][t]=next_number
        tree[next_y][next_t]=None
        tree[next_number]=[left,right]


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
            if root==None:
                root=number
                tree[number]=[None,None,None]
            else:
                tree[number]=[None,None,None]
                insert(tree,number)
            
        elif tmp[0]=="find":
            if find(root,number) is not None:
                print("yes")
            else:
                print("no")
        
        else:
            delete(tree,number)

