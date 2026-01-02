# Rooted Trees

import sys
sys.setrecursionlimit(2**20)  # 再帰回数上限の向上 かなり多くしないとREになる

class Node:
    def __init__(self, parent, left, right):
        self.parent = parent
        self.left = left
        self.right = right

def get_depth(T: dict, u: int):
    d = 0
    while T[u].parent is not None:
        u = T[u].parent
        d += 1
    return d

D = {}  # 深さを保存しておく用のdict

def get_all_depth(T: dict, u: int, p: int):
    '''  
    一度にすべてのノードの深さを取得する関数(再帰的に処理を行う)。
    一気に全体の深さを求めるならばこちらの方がオーダーが小さい。
    pは現在扱う深さ
    '''
    D[u] = p
    if T[u].right is not None:
        # 右の兄弟ノード(深さは同じ)から入れていく
        get_all_depth(T, T[u].right, p)
    if T[u].left is not None:
        # 兄弟を入れ終わったら次は下のふさへ
        get_all_depth(T, T[u].left, p+1)

def ret_children(T, u):
    children = []
    c = T[u].left
    while c is not None:
        children.append(c)
        c = T[c].right
    return children

def print_for_a_node(T: dict, node: int, D: dict):
    node_type = 'internal node' if T[node].left is not None else 'leaf'
    if T[node].parent is None:
        parent = -1
        node_type = 'root'
    else:
        parent = T[node].parent
    children = ret_children(T, node)

    print(
        f'node {node}: parent = {parent}, depth = {D[node]}, {node_type}, {children}')

N = int(input())
T = {k: Node(None, None, None) for k in range(N)}
for _ in range(N):
    lst = list(map(int, input().split()))
    if lst[1] == 0:  # もし子ノードがなければ次へ
        continue
    T[lst[0]].left = lst[2]
    T[lst[2]].parent = lst[0]
    prev_sibling = lst[2]  # 前のノード番号を覚えておく用
    for sib in lst[3:]:
        T[prev_sibling].right = sib
        T[sib].parent = lst[0]  # 子から親を与えている
        prev_sibling = sib

for node in range(N):
    if T[node].parent is None:
        get_all_depth(T, node, 0)  # rootを入れなければいけないことに注意
        # Dに深さが入った
        break

for node in range(N):
    print_for_a_node(T, node, D)
