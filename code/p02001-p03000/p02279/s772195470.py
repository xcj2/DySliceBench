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
    if T[u].right != -1:
        get_all_depth(T, T[u].right, p)
    if T[u].left != -1:
        get_all_depth(T,T[u].left,p+1)

def ret_children(T,u):
    children = []
    c = T[u].left
    while c != -1:
        children.append(c)
        c = T[c].right
    return children

def print_for_a_node(T:dict,node:int,D:dict):
    node_type = "leaf" if T[node].left == -1 else "internal node"
    if T[node].parent == -1:
        node_type = "root"
    parent = T[node].parent
    children = ret_children(T,node)
    print(f"node {node}: parent = {parent}, depth = {D[node]}, {node_type}, {children}")

n = int(input())

T = {k: Node(-1,-1,-1) for k in range(n)}

for _ in range(n):
    tmp = list(map(int,input().split()))
    if  tmp[1] == 0:
        continue
    T[tmp[0]].left = tmp[2]
    T[tmp[2]].parent = tmp[0]
    prev_sibling = tmp[2]
    for sib in tmp[3:]:
        T[prev_sibling].right = sib
        T[sib].parent = tmp[0]
        prev_sibling = sib

for node in range(n):
    if T[node].parent == -1:
        get_all_depth(T,node,0)
        break

for node in range(n):
    print_for_a_node(T,node,D)
