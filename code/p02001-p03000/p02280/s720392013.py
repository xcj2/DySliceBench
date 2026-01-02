class node:
    def __init__(self, parent, left, right, depth, height):
        self.p = parent
        self.l = left
        self.r = right
        self.d = depth
        self.h = height

def setDepth(u, depthPosition):
    if u == -1:
        return
    T[u].d = depthPosition
    setDepth(T[u].r, depthPosition + 1)
    setDepth(T[u].l, depthPosition + 1)

def setHeight(u):
    h1 = h2 = 0
    if T[u].r != -1:
        h1 = setHeight(T[u].r) + 1
    if T[u].l != -1:
        h2 = setHeight(T[u].l) + 1
    T[u].h = max(h1, h2)
    return max(h1, h2)

def getDegree(u):
    degree = 0
    if T[u].r != -1:
        degree += 1
    if T[u].l != -1:
        degree += 1
    return degree

def getSibling(u):
    if T[u].p == -1:
        return -1
    if T[T[u].p].l != u and T[T[u].p].l != -1:
        return T[T[u].p].l
    if T[T[u].p].r != u and T[T[u].p].r != -1:
        return T[T[u].p].r
    return -1    

n = int(input())
T = [node(-1, -1, -1, 0, 0) for _ in range(n)]
for _ in range(n):
    info = list(map(int, input().split(" ")))
    T[info[0]].l = info[1]
    T[info[0]].r = info[2]
    if info[1] != -1:
        T[info[1]].p = info[0]
    if info[2] != -1:
        T[info[2]].p = info[0]

for x in T:
    if x.p == -1:
        setDepth(T.index(x), 0)
        setHeight(T.index(x))

for i in range(n):
    print("node", end = ' ')
    print(i, end = ': ')
    print("parent =", end = ' ')
    print(T[i].p, end = ', ')
    print("sibling =", end = ' ')
    print(getSibling(i), end = ', ')
    print("degree =", end = ' ')
    print(getDegree(i), end = ', ')
    print("depth =", end = ' ')
    print(T[i].d, end = ', ')
    print("height =", end = ' ')
    print(T[i].h, end = ', ')
    if T[i].p == -1: print("root")
    elif T[i].r == -1 and T[i].l == -1: print("leaf")
    else: print("internal node")

