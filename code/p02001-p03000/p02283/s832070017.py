# Bibary Search Tree

import sys
sys.setrecursionlimit(2**20)  # 再帰回数上限の向上 かなり多くしないとREになる

root = None

class Node:
    def __init__(self,
                 parent=None,
                 left=None,
                 right=None):
        self.parent = parent
        self.left = left  # 左の子ノード
        self.right = right  # 右の子ノード

# 先行順巡回
def pre_parse(T: dict, u: int, pre_ls: list):
    # 深さ優先探索特有の即時終了条件
    if u == None:
        return
    pre_ls.append(u)
    pre_parse(T, T[u].left, pre_ls)  # より左の方から深さ優先探索
    pre_parse(T, T[u].right, pre_ls)

# 中間順巡回
def in_parse(T, u, in_ls):
    if u == None:
        return
    # 左→中→右の順に巡回
    in_parse(T, T[u].left, in_ls)
    in_ls.append(u)
    in_parse(T, T[u].right, in_ls)

# 挿入
def insert(T, z):
    global root
    T[z] = Node()
    y = None # xの親
    x = root # Tの根
    while (x is not None):
        y = x # xの親を設定
        if z < x:
            x = T[x].left # 左の子へ移動
        else:
            x = T[x].right # 右の子へ移動
    T[z].parent = y # zの親にyを設定
    if (y is None):
        root = z
    elif (z < y):
        T[y].left = z # yの左の子にする
    else:
        T[y].right = z # yの右の子にする


def find(T,  ROOT, k):
    x = ROOT # 訪問中のノード
    while T[x] is not None and x != k:
        if (k < x):
            T[x].left = x
        else:
            T[x].right = x
    return x

def print_result(T):
    pre_ls, in_ls = [], []
    in_parse(T, root, in_ls)
    pre_parse(T, root, pre_ls)
    print('', *in_ls)
    print('', *pre_ls)

N = int(input())
lst = [input().split() for i in range(N)]
T = {}
for i, c in enumerate(lst):
    if c[0] == 'insert':
        z = int(c[1])
        insert(T, z)
    elif c[0] == 'print':
        print_result(T)
    elif c[0] == 'find':
        is_find = find(T, root, z)
        if is_find is None:
            print('no')
        else:
            print('Yes')
