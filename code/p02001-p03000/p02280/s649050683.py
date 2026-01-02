import sys
from typing import no_type_check_decorator
sys.setrecursionlimit(2**20)

class Node:
    def __init__(self, parent, left, right):
        self.parent = parent
        self.left = left #左の子ノード
        self.right = right #右の子ノード

def get_all_height(T: dict, H: dict, u: int):
    """
    深さ優先探索で各ノードを巡りながらHに高さ情報を容れる
    """
    h_left, h_right = 0, 0
    if T[u].left is not None:
        h_left = get_all_height(T, H, T[u].left) + 1
    if T[u].right is not None:
        h_right = get_all_height(T, H, T[u].right) + 1
    
    ret = max(h_left, h_right)
    H[u] = ret
    return ret

def get_all_depth(T: dict, D: dict, u: int, p: int):
    """
    D: 深さを格納する辞書
    p: 現在の深さ
    """
    D[u] = p
    if T[u].left is not None:
        get_all_depth(T, D, T[u].left, p+1)
    if T[u].right is not None:
        get_all_depth(T, D, T[u].right, p+1)

def ret_sibling(T: dict, u: int):
    """
    ノードuの兄弟を返す
    """
    parent = T[u].parent
    if parent is None:
        return -1 # root は兄弟なし
    # 自分のparentから見て子ノードはleft or rightの二つ。
    # 自分自身(ノードu)に一致していない方を返す
    ret = T[parent].left if T[parent].left != u else T[parent].right
    if ret is None: #兄弟がいない場合
        return -1
    return ret

def ret_degree(T: dict, u: int):
    ret = 2
    if T[u].left is None:
        ret -= 1
    if T[u].right is None:
        ret -= 1
    return ret


# input
n = int(input())
T = {key: Node(None, None, None) for key in range(n)}
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
        ROOT = k # 根を探す
        break 

D = {}
get_all_depth(T, D, ROOT, 0)
H = {}
get_all_height(T, H, ROOT)

def print_for_a_node(u):
    if T[u].parent is None:
        parent = -1
    else:
        parent = T[u].parent
    
    sib = ret_sibling(T, u)
    deg = ret_degree(T, u)
    node_type = "internal node" if deg != 0 else "leaf"
    if parent == -1:
        node_type = "root"
    
    print(
        f"node {u}: parent = {parent}, sibling = {sib}, degree = {deg}, depth = {D[u]}, height = {H[u]}, {node_type}"
    )

for node in range(n):
    print_for_a_node(node)
