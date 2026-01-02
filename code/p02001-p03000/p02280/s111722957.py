class Node():
    def __init__(self):
        self.parent = -1
        self.left = -1
        self.right = -1
        self.depth = 0
        self.sibling = -1
        self.degree = 0
        self.height = -1
        return

def getAncestor(t, n):
    for i in range(n):
        if t[i].parent == -1:
            return i

def setDepth(t, u, p=0):#u : 自分ノードの番号
    t[u].depth = p
    if t[u].left != -1:
        setDepth(t, t[u].left,p+1)
    if t[u].right != -1:
        setDepth(t, t[u].right,p+1)
    return

def seeHeight(h, u):
    h1 = 0
    h2 = 0
    if t[u].right != -1:
        h1 = seeHeight(t[u].height, t[u].right) + 1
    if t[u].left != -1:
        h2 = seeHeight(t[u].height, t[u].left) + 1

    t[u].height = max(h1, h2)
    return t[u].height

import sys

n = int(input())
t = []
for _ in range(n):
    t.append(Node())

for i in range(n):
    a = list(map(int, sys.stdin.readline().split()))
    m = a[0]
    t[m].left = a[1]
    t[m].right = a[2]
    if a[1] != -1:
        t[m].degree += 1
        t[a[1]].parent = m
        t[a[1]].sibling = a[2]
    if a[2] != -1:
        t[m].degree += 1
        t[a[2]].parent = m
        t[a[2]].sibling = a[1]

r = getAncestor(t, n)
setDepth(t, r)
seeHeight(-1, r)

for i in range(n):
    if i == r:
        print('node {0}: parent = {1}, sibling = {2}, degree = {3}, depth = {4}, height = {5}, root'.format(i, t[i].parent, t[i].sibling, t[i].degree, t[i].depth, t[i].height))
    elif t[i].degree == 0:
        print('node {0}: parent = {1}, sibling = {2}, degree = {3}, depth = {4}, height = {5}, leaf'.format(i, t[i].parent, t[i].sibling, t[i].degree, t[i].depth, t[i].height))
    else:
        print('node {0}: parent = {1}, sibling = {2}, degree = {3}, depth = {4}, height = {5}, internal node'.format(i, t[i].parent, t[i].sibling, t[i].degree, t[i].depth, t[i].height))


