from sys import stdin
N=int(input())
nodes=[None]*N
oya=[None]
class node_tree():
    def __init__(self,node):
        self.node=node
        self.parent=None
        self.left=None
        self.right=None
        self.brother=None
        self.up=None

def ino(u):

    if u.left is not None:
        ino(u.left)
    print("",u.node,end="")
    if u.right is not None:
        ino(u.right)
def pre(u):
    print("",u.node,end="")
    if u.left is not None:
        pre(u.left)
    if u.right is not None:
        pre(u.right)
def search(u,key):
    if u.node <=key.node:
        if u.right is not None:
            u.right.parent=u
            search(u.right,key)
        else:
            u.right=key
            u.right.parent=u
    else:
        if u.left is not None:
            u.left.parent=u
            search(u.left,key)
        else:
            u.left=key
            u.left.parent = u
def find(u,key):
    if u.node==key:
        print("yes",end="")
        return
    if u.node < key:
        if u.right is not None:
            find(u.right, key)
        else:
            print("no",end="")
            return
    else:
        if u.left is not None:
            find(u.left, key)
        else:
            print("no",end="")
            return
def delete_find(u,key):
    if u.node==key:
        return u
    if u.node < key:
        if u.right is not None:
            return delete_find(u.right, key)
    else:
        if u.left is not None:
            return delete_find(u.left, key)
def get(u):#次の次節点を探す
    if u.right is not None:
        return getMini(u.right)
    # y=u.parent
    # while (y is not None and u==y.right):
    #     u=y
    #     y=y.parent
    # return y
def getMini(u):
    while u.left is not None:
        u=u.left
    return u
def delete(z):
    if z.left is None or z.right is None:
        y=z
    else:
        y=get(z)
    if y.left is not None:
        x=y.left
    else:
        x=y.right
    if x is not None:
        x.parent=y.parent
    if y.parent is None:
        oya[0]=x
    elif y==y.parent.left:
        y.parent.left=x
    else:
        y.parent.right=x
    if y!=z:
        z.node=y.node
command_list=[]*N
for i in range(N):
    command_list.append((stdin.readline().strip().split()))
for i,command in enumerate(command_list):
    if len(command)!=1:
        if command[0]=="find":
            find(nodes[0],int(command[1]))
            print()
        elif command[0]=="delete":
            key=int(command[1])
            if oya[0] is None:
                z=delete_find(nodes[0],key)
            else:
                z=delete_find(oya[0],key)
            delete(z)
        else:
            key=int(command[1])
            if i==0:
                nodes[i]=node_tree(key)
            else:
                ins=node_tree(key)
                if oya[0] is None:
                    search(nodes[0],ins)
                    nodes[i]=ins
                else:
                    search(oya[0],ins)
                    nodes[i]=ins
    else:
        if oya[0] is None:
            ino(nodes[0])
            print()
            pre(nodes[0])
            print()
        else:
            ino(oya[0])
            print()
            pre(oya[0])
            print()


