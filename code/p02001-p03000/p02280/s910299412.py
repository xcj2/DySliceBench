import sys
sys.setrecursionlimit(10**7)

class Node:
    def __init__(self, parent, left, right):
        self.parent = parent
        self.left = left  
        self.right = right

def get_height(T, H, u):
    h1, h2 = 0, 0
    if T[u].right is not None:
        h1 = get_height(T, H, T[u].right) + 1
    if T[u].left is not None:
        h2 = get_height(T, H, T[u].left) + 1
    h = max(h1, h2)
    H[u] = h
    return h


def get_depth(T, D, u, d):
    D[u] = d
    if T[u].right is not None:
        get_depth(T, D, T[u].right, d+1) 
    if T[u].left is not None:
        get_depth(T, D, T[u].left, d+1) 

def ret_sibling(T, u):
    parent = T[u].parent
    if parent is None:
        return -1
    if T[parent].left != u:
        ret = T[parent].left
    else:
        ret = T[parent].right
    if ret is None:
        return -1
    return ret

def ret_degree(T, u):
    ret = 2
    if T[u].left is None:
        ret -= 1
    if T[u].right is None:
        ret -= 1
    return ret

n = int(input())
T = {k: Node(None, None, None) for k in range(n)}  
for _ in range(n):
    tmp = list(map(int, input().split()))
    if tmp[1] != -1:
        T[tmp[0]].left = tmp[1]  
        T[tmp[1]].parent = tmp[0]  
    if tmp[2] != -1:
        T[tmp[0]].right = tmp[2]  
        T[tmp[2]].parent = tmp[0]

for k, v in T.items():
    if v.parent is None:
        ROOT = k
        break

D = {}
get_depth(T, D, ROOT, 0)
H = {}
get_height(T, H, ROOT)


def print_for_a_node(u):
    if T[u].parent is None:
        parent = -1
    else:
        parent = T[u].parent

    sib = ret_sibling(T, u)
    deg = ret_degree(T, u)
    node_type = 'internal node' if deg != 0 else 'leaf'
    if parent == -1:
        node_type = 'root'

    print(f'node {u}: parent = {parent}, sibling = {sib}, degree = {deg}, depth = {D[u]}, height = {H[u]}, {node_type}')


for node in range(n):
    print_for_a_node(node)
