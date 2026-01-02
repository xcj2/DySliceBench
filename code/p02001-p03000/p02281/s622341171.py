import sys
sys.setrecursionlimit(10**6) 

class Node:
    def __init__(self, parent, left, right):
        self.p = parent
        self.l = left
        self.r = right


n = int(input())
node = {}
for i in range(n):
    node[i] = Node(-1, -1, -1)


for j in range(n):
    temp = list(map(int, input().split()))
    if temp[1] != -1:
        node[temp[0]].l = temp[1]
        node[temp[1]].p = temp[0]
    if temp[2] != -1:
        node[temp[0]].r = temp[2]
        node[temp[2]].p = temp[0]


def pre_parse(T, u, pre_list):
    if u == -1:
        return
    pre_list.append(u)
    pre_parse(T, T[u].l, pre_list)
    pre_parse(T, T[u].r, pre_list)

def in_parse(T, u, in_list):
    if u == -1:
        return
    in_parse(T, T[u].l, in_list)
    in_list.append(u)
    in_parse(T, T[u].r, in_list)

def post_parse(T, u, post_list):
    if u == -1:
        return
    post_parse(T, T[u].l, post_list)
    post_parse(T, T[u].r, post_list)
    post_list.append(u)


for k, v in node.items():
    if v.p == -1:
        root = k

pre_list = []
in_list = []
post_list = []
pre_parse(node, root, pre_list)
in_parse(node, root, in_list)
post_parse(node, root, post_list)

print('Preorder')
print('', *pre_list)
print('Inorder')
print('', *in_list)
print('Postorder')
print('', *post_list)
