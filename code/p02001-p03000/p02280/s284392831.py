import sys
sys.setrecursionlimit(2**20)

class Node():
    def __init__(self,parent,left,right):
        self.parent = parent
        self.left = left
        self.right = right

def get_all_height(T: dict, H: dict, u: int):
    #深さ優先探索で各地点をめぐりながらHに高さ情報をセットしていく
    h_left = 0
    h_right = 0
    if T[u].left is not None:
        h_left = get_all_height(T,H,T[u].left) + 1
    if T[u].right is not None:
        h_right = get_all_height(T,H,T[u].right) + 1

    ret = max(h_left,h_right)
    H[u] = ret
    return ret

def get_all_depth(T, D:dict, u:int, p:int):
    D[u] = p
    if T[u].left is not None:
        get_all_depth(T,D,T[u].left,p+1)
    if T[u].right is not None:
        get_all_depth(T,D,T[u].right,p+1)

def ret_sibling(T,u):
    parent = T[u].parent
    if parent == None:
        return -1
    if T[parent].left == u:
        ret = T[parent].right
    else:
        ret = T[parent].left

    if ret == None:
        return -1

    return ret

def ret_degree(T,u):
    ret = 0
    if T[u].left != None:
        ret += 1
    if T[u].right != None:
        ret += 1
    return ret

#データを読み込む
n = int(input())
T = {key: Node(None,None,None) for key in range(n)}
for _ in range(n):
    tmp = list(map(int,input().split()))

    if tmp[1] != -1:
        T[tmp[0]].left = tmp[1]
        T[tmp[1]].parent = tmp[0]
    if tmp[2] != -1:
        T[tmp[0]].right = tmp[2]
        T[tmp[2]].parent = tmp[0]

#根の探索
for i in range(n):
    if T[i].parent is None:
        ROOT = i
        break
else:
    raise ValueError("ROOTが存在しないなんておかしい")

#深さと高さの探索
D = {}
get_all_depth(T,D,i,0)
H = {}
get_all_height(T,H,ROOT)

def print_for_a_node(u):
    if T[u].parent is None:
        parent = -1
    else:
        parent = T[u].parent

    sib = ret_sibling(T,u)
    deg = ret_degree(T,u)
    node_type = 'internal node' if deg != 0 else 'leaf'
    if parent == -1:
        node_type = 'root'

    print(f'node {u}: parent = {parent}, sibling = {sib}, degree = {deg}, depth = {D[u]}, height = {H[u]}, {node_type}')

for node in range(n):
    print_for_a_node(node)

