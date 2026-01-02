import sys
sys.setrecursionlimit(10**7)

class Node:
    def __init__(self,parent,left,right):
        self.parent = parent
        self.left = left
        self.right = right

def get_depth(T:dict,u:int):
    d = 0
    while T[u] != -1:
        u = T[u].parent
        d += 1

D = {}

def get_all_depth(T:dict,u:int,p:int):
    D[u] = p
    if T[u].left != -1:
        get_all_depth(T,T[u].left,p+1)
    if T[u].right != -1:
        get_all_depth(T,T[u].right,p+1)

H = {}

def get_all_height(T:dict,u:int):
    h1 = 0
    h2 = 0
    if T[u].right != -1:
        h1 = get_all_height(T,T[u].right)+1
    if T[u].left != -1:
        h2 = get_all_height(T,T[u].left)+1
    H[u] = max(h1,h2)
    return H[u]

def get_sibling(T:dict,u:int):
    if T[u].parent == -1:
        return -1
    if T[T[u].parent].left != u and T[T[u].parent].left != -1:
        return T[T[u].parent].left
    if T[T[u].parent].right != u and T[T[u].parent].right != -1:
        return T[T[u].parent].right
    return -1

def PRINT(T:dict,node:int,D:dict,H:dict):
    dig = (T[node].right!=-1)+(T[node].left!=-1)
    if (T[node].left==-1) and (T[node].right==-1):
        node_type = "leaf"
    else:
        node_type = "internal node"
    if T[node].parent == -1:
        node_type = "root"
    print(f"node {node}: parent = {T[node].parent}, sibling = {get_sibling(T,node)}, degree = {dig}, depth = {D[node]}, height = {H[node]}, {node_type}")

n = int(input())
T = {k: Node(-1,-1,-1) for k in range(n)}
    
for _ in range(n):
    a,b,c = map(int,input().split())
    T[a].left = b
    T[a].right = c
    if b != -1:
        T[b].parent = a
    if c != -1:
        T[c].parent = a
for node in range(n):
    if T[node].parent == -1:
        get_all_depth(T,node,0)
        get_all_height(T,node)
        break
for node in range(n):
    PRINT(T,node,D,H)
