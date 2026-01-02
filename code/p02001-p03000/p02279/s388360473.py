import sys
sys.setrecursionlimit(10**7)

class Node:
    def __init__(self, parent, left, right):
        self.parent = parent
        self.left = left  
        self.right = right

D = {}  

def get_all_depth(T: dict, u: int, p: int):
    D[u] = p
    if T[u].right is not None:
        get_all_depth(T, T[u].right, p)
    if T[u].left is not None:
        get_all_depth(T, T[u].left, p+1)

def ret_children(T, u):
    chilren = []
    c = T[u].left
    while c is not None:
        chilren.append(c)
        c = T[c].right
    return chilren

def print_for_a_node(T, node, D):
    if T[node].left is not None: 
        node_type = 'internal node'
    else:
        node_type = 'leaf'
        
    if T[node].parent is None:
        parent = -1
        node_type = 'root'
    else:
        parent = T[node].parent
        
    children = ret_children(T, node)
    print(f'node {node}: parent = {parent}, depth = {D[node]}, {node_type}, {children}')


n = int(input())

T = {k: Node(None, None, None) for k in range(n)}  

for _ in range(n):
    tmp = list(map(int, input().split()))
    if tmp[1] != 0:  
        T[tmp[0]].left = tmp[2]  
        T[tmp[2]].parent = tmp[0]  
        prev_sibling = tmp[2]  
        
        for sib in tmp[3:]:
            T[prev_sibling].right = sib
            T[sib].parent = tmp[0] 
            prev_sibling = sib

for node in range(n):
    if T[node].parent is None:
        get_all_depth(T, node, 0)  
        break

for node in range(n):
    print_for_a_node(T, node, D)
