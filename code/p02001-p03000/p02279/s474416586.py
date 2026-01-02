class Node():
    def __init__(self, p, l, r, deg):
        self.parent = p
        self.left = l
        self.right = r
        self.deg = deg

def GetDepth(T, u):
    d = 0
    while T[u].parent != -1:
        u = T[u].parent
        d += 1
    return d

def SetDepth(D, T, u, p):
    D[u] = p
    if T[u].right != -1:
        SetDepth(D, T, T[u].right, p)
    if T[u].left != -1:
        SetDepth(D, T, T[u].left, p + 1)

def GetChildren(T, u):
    children = list()
    c = T[u].left
    while c != -1:
        children.append(str(c))
        c = T[c].right
    
    return children

def Main():

    n = int(input())

    T = [Node(-1, -1, -1, 0) for i in range(n)]
    D = [0]*n

    for i in range(n):
        node_id, k, *children = map(int, input().split())
        T[node_id].deg = k

        if k > 0 :
            T[node_id].left = children[0]

            for i in range(k):
                T[children[i]].parent = node_id
                
                if i + 1 <= k - 1:
                    T[children[i]].right = children[i + 1]

    for i in range(len(T)):
        D[i] = GetDepth(T, i)

    for i in range(len(T)):
        t = T[i]
        node_type = ""

        if t.parent == -1:
            node_type = "root"
        elif t.deg == 0:
            node_type = "leaf"
        else:
            node_type = "internal node"

        print("node {0}: parent = {1}, depth = {2}, {3}, {4}".format(i, t.parent, D[i], node_type, "[" + ", ".join(GetChildren(T, i)) + "]"))

Main()
