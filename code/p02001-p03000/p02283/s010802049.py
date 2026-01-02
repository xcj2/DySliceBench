import sys
sys.setrecursionlimit(10**7)

class Node:
    def __init__(self,parent,left,right):
        self.parent = parent
        self.left = left
        self.right = right

def insert(T:dict,z:int):
    global root
    y = -1
    x = root
    while x != -1:
        y = x
        if z < x:
            x = T[x].left
        else:
            x = T[x].right
    T[z] = Node(y,-1,-1)
    
    if y == -1:
        root= z
    elif z < y:
        T[y].left = z
    else:
        T[y].right = z

def inorder(u:int):
    if u == -1:
        return 
    inorder(T[u].left)
    print(" "+str(u),end="")
    inorder(T[u].right)

def preorder(u:int):
    if u == -1:
        return 
    print(" "+str(u),end="")
    preorder(T[u].left)
    preorder(T[u].right)

n = int(input())
root = -1
T = {}
for _ in range(n):
    scan = input().split()
    if len(scan) == 1:
        inorder(root)
        print()
        preorder(root)
        print()
    else:
        insert(T,int(scan[-1]))
