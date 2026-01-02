import sys
sys.setrecursionlimit(2**20)

class Node:
    def __init__(self, parent, left, right):
        self.parent = parent #親
        self.left = left #一番左の子ノード
        self.right = right #すぐ右の兄弟

def get_depth(T: dict, u: int):
    """
    T: 木構造
    u: ノード番号
    """
    d = 0
    while T[u].parent is not None:
        u = T[u].parent
        d += 1

D = {} #深さを保存

def get_all_depth(T: dict, u: int, p: int):
    """
    一度に全てのノードの深さを再帰的に取得する。
    p: 現在扱う深さ
    """
    D[u] = p
    if T[u].right is not None:
        get_all_depth(T, T[u].right, p) #兄弟から入れていく（深さは同じ）
    if T[u].left is not None:
        get_all_depth(T, T[u].left, p+1) #1つ深く潜る

def ret_children(T: dict, u: int):
    children = []
    c = T[u].left
    while c is not None:
        children.append(c)
        c = T[c].right
    return children

# 答え出力
def print_for_a_node(T: dict, node: int, D: dict):
    node_type = "internal node" if T[node].left is not None else "leaf"
    if T[node].parent is None: #親ノードが無ければ
        parent = -1
        node_type = "root"
    else:
        parent = T[node].parent
    children = ret_children(T, node)
    print(
        f"node {node}: parent = {parent}, depth = {D[node]}, {node_type}, {children}"
    )

# 入力
n = int(input())

T = {k: Node(None, None, None) for k in range(n)}

for _ in range(n):
    tmp = list(map(int, input().split()))
    if tmp[1] == 0: # 子ノードがなければ次へ
        continue
    T[tmp[0]].left = tmp[2] # 一番左の子ノード
    T[tmp[2]].parent = tmp[0] # 子ノードの親（自分）
    prev_sibling = tmp[2]
    for sib in tmp[3:]:
        T[prev_sibling].right = sib
        T[sib].parent = tmp[0]
        prev_sibling = sib

for node in range(n):
    if T[node].parent is None:
        get_all_depth(T, node, 0)
        # Dに深さが格納された
        break
for node in range(n):
    print_for_a_node(T, node, D)
