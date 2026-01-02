import sys
sys.setrecursionlimit(2 ** 20)

class Node():
    def __init__(self, parent=None, left=None, right=None):
        self.parent = parent
        self.left = left
        self.right = right

    def __repr__(self):
        return '<Node object: parent={}, left={}, right={}>' .format(self.parent, self.left, self.right)


def set_depth(u, p):
    D[u] = p
    if not T[u].right is None:
        set_depth(T[u].right, p)
    if not T[u].left is None:
        set_depth(T[u].left, p+1)


def get_children(u):
    res = []
    c = T[u].left
    while c is not None:
        res.append(c)
        c = T[c].right
    return res


def get_type(node):
    if node.parent is None:
        return 'root'
    elif node.left is None:
        return 'leaf'
    else:
        return 'internal node'


def get_parent(node):
    return -1 if node.parent is None else node.parent


n = int(input())
T = [Node() for i in range(n)]
for _ in range(n):
    line = list(map(int, input().split()))
    i, k = line[:2]
    if k:
        T[i].left = line[2]
        prev = None
        for c in line[2:]:
            T[c].parent = i
            if prev:
                T[prev].right = c
            prev = c

D = [0] * n
for i in range(n):
    if T[i].parent is None:
        set_depth(i, 0)
        break

for i in range(n):
    print('node {}: parent = {}, depth = {}, {}, {}'.format(
        i, get_parent(T[i]), D[i], get_type(T[i]), get_children(i)))
