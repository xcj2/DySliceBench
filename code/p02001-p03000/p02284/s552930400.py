from sys import stdin
N=int(input())
nodes=[None]*N
class node_tree():
    def __init__(self,node):
        self.node=node
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
            search(u.right,key)
        else:u.right=key
    else:
        if u.left is not None:
            search(u.left,key)
        else:u.left=key
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
command_list=[]*N
for i in range(N):
    command_list.append((stdin.readline().strip().split()))
for i,command in enumerate(command_list):
    if len(command)!=1:
        if command[0]=="find":
            find(nodes[0],int(command[1]))
            print()
        else:
            key=int(command[1])
            if i==0:
                nodes[i]=node_tree(key)
            else:
                ins=node_tree(key)
                search(nodes[0],ins)
                nodes[i]=ins
    else:
        ino(nodes[0])
        print()
        pre(nodes[0])
        print()


