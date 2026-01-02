import sys

sys.setrecursionlimit(2 ** 20)  # 再帰回数上限の向上 かなり多くしないとREになる


class Node:
    def __init__(self,
                 left,
                 right):
        self.left = left
        self.right = right


def insert(t: dict, i: int, r: int):
    if r > i:
        if t[r].left is not None:
            insert(t, i, t[r].left)
        else:
            t[r].left = i
    if r < i:
        if t[r].right is not None:
            insert(t, i, t[r].right)
        else:
            t[r].right = i


def inorder(t: dict, p: int, in_ls: list):
    if t[p].left is not None:
        inorder(t, t[p].left, in_ls)
    in_ls.append(p)
    if t[p].right is not None:
        inorder(t, t[p].right, in_ls)


def preorder(t: dict, p: int, pre_ls: list):
    pre_ls.append(p)
    if t[p].left is not None:
        preorder(t, t[p].left, pre_ls)
    if t[p].right is not None:
        preorder(t, t[p].right, pre_ls)


N = int(input())
T = {}
in_list = []
pre_list = []

order = list(map(str, input().split()))
root = int(order[1])
T[root] = Node(None, None)

for _ in range(N-1):
    order = str(input())
    if order[0] == 'i':
        order = list(order.split())
        T[int(order[1])] = Node(None, None)
        insert(T, int(order[1]), root)
    elif order[0] == 'f':
        order = list(order.split())
        if int(order[1]) in T:
            print('yes')
        else:
            print('no')
    else:
        inorder(T, root, in_list)
        print('', *in_list)
        preorder(T, root, pre_list)
        print('', *pre_list)
        in_list = []
        pre_list = []

