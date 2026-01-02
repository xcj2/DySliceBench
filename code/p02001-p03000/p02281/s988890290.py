import sys

sys.setrecursionlimit(2 ** 20)  # 再帰回数上限の向上 かなり多くしないとREになる


class Node:
    def __init__(self,
                 parent,
                 left,
                 right):
        self.parent = parent
        self.left = left
        self.right = right


n = int(input())
T = {key: Node(None, None, None) for key in range(n)}  # 初期化
for _ in range(n):
    tmp = list(map(int, input().split()))
    # 左から処理
    if tmp[1] != -1:
        T[tmp[0]].left = tmp[1]  # 子の代入
        T[tmp[1]].parent = tmp[0]  # 親の代入
    if tmp[2] != -1:
        T[tmp[0]].right = tmp[2]  # 子の代入
        T[tmp[2]].parent = tmp[0]  # 親の代入


def preorder(t: dict, p: int, pre_ls: list):
    pre_ls.append(p)
    if t[p].left is not None:
        preorder(t, t[p].left, pre_ls)
    if t[p].right is not None:
        preorder(t, t[p].right, pre_ls)


def inorder(t: dict, p: int, in_ls: list):
    if t[p].left is not None:
        inorder(t, t[p].left, in_ls)
    in_ls.append(p)
    if t[p].right is not None:
        inorder(t, t[p].right, in_ls)


def postorder(t: dict, p: int, post_ls: list):
    if t[p].left is not None:
        postorder(t, t[p].left, post_ls)
    if t[p].right is not None:
        postorder(t, t[p].right, post_ls)
    post_ls.append(p)


for id, node in T.items():
    if node.parent is None:
        ROOT = id

a, b, c = [], [], []
preorder(T, ROOT, a)
inorder(T, ROOT, b)
postorder(T, ROOT, c)

print('Preorder')
print('', *a)
print('Inorder')
print('', *b)
print('Postorder')
print('', *c)

