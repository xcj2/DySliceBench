# Binary tree 二分木の表現


class Node():
    
    def __init__(self):
        self.parent = -1
        self.left = -1
        self.right = -1


def settype(u):
    if T[u].parent == -1:
        Type[u] = "root"
    elif Deg[u] == 0:
        Type[u] = "leaf"
    else:
        Type[u] = "internal node"


def setdepth(u, p):
    Dep[u] = p
    if T[u].left != -1:
        setdepth(T[u].left, p + 1)
    if T[u].right != -1:
        setdepth(T[u].right, p + 1)


def setheight(u):
    hl, hr = 0, 0
    if T[u].left != -1:
        hl = setheight(T[u].left) + 1
    if T[u].right != -1:
        hr = setheight(T[u].right) + 1
    H[u] = max(hl, hr)
    return H[u]


n = int(input())
T = [Node() for i in range(n)]
S = [-1 for i in range(n)]
Deg = [0 for i in range(n)]

for i in range(n):
    id, left, right = (int(j) for j in input().split())
    if left != -1:
        T[id].left = left
        T[left].parent = id
        S[left] = right
        Deg[id] += 1
    if right != -1:
        T[id].right = right
        T[right].parent = id
        S[right] = left
        Deg[id] += 1

rootid = -1

for id in range(n):
    if T[id].parent == -1:
        rootid = id
        break

Dep = [-1 for i in range(n)]
setdepth(rootid, 0)

Type = ["" for i in range(n)]
for id in range(n):
    settype(id)

H = [-1 for i in range(n)]
setheight(rootid)

for id in range(n):
    print("node ", id, ": parent = ", T[id].parent, ", sibling = ", S[id], ", degree = ", Deg[id], ", depth = ", Dep[id], ", height = ", H[id], ", ", Type[id], sep="")

