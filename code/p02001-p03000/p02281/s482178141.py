import sys
sys.setrecursionlimit(2**20)

class Node:
    def __init__(self, parent,
                left, right) -> None:
        self.parent = parent
        self.left = left
        self.right = right

def pre_parse(T: dict, u: int, pre_ls: list):
    if u is None:
        return
    pre_ls.append(u)
    pre_parse(T, T[u].left, pre_ls)
    pre_parse(T, T[u].right, pre_ls)

def in_parse(T: dict, u: int, in_ls: list):
    if u is None:
        return
    in_parse(T, T[u].left, in_ls)
    in_ls.append(u)
    in_parse(T, T[u].right, in_ls)

def post_parse(T: dict, u: int, post_ls: list):
    if u is None:
        return
    post_parse(T, T[u].left, post_ls)
    post_parse(T, T[u].right, post_ls)
    post_ls.append(u)

# input
n = int(input())
T = {key: Node(None, None, None) for key in range(n)}
for _ in range(n):
    tmp = list(map(int, input().split()))
    T[tmp[0]].left = tmp[1] if tmp[1] != -1 else None
    T[tmp[0]].right = tmp[2] if tmp[2] != -1 else None
    if tmp[1] != -1:
        T[tmp[1]].parent = tmp[0]
    if tmp[2] != -1:
        T[tmp[2]].parent = tmp[0]
ROOT = 0
for id, node in T.items():
    if node.parent is None:
        ROOT = id
        break

pre_ls, in_ls, post_ls = [], [], []
pre_parse(T, ROOT, pre_ls)
in_parse(T, ROOT, in_ls)
post_parse(T, ROOT, post_ls)

print("Preorder")
print("", *pre_ls)
print("Inorder")
print("", *in_ls)
print("Postorder")
print("", *post_ls)
