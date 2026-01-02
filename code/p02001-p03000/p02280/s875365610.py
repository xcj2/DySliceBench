class Node():
    def __init__(self, parent, left, right, sibling, degree):
        self.parent = parent
        self.left = left
        self.right = right
        self.sibling = sibling
        self.degree = degree

def GetDepth(T, u):
    d = 0
    n = T[u]

    while n.parent != -1:
        n = T[n.parent]
        d += 1

    return d

def GetHight(T, u, d):

    if T[u].left != -1:
        h1 = GetHight(T, T[u].left, d + 1)
    else:
        h1 = d

    if T[u].right != -1:
        h2 = GetHight(T, T[u].right, d + 1)
    else:
        h2 = d

    return max(h1, h2)

def Main():

    n = int(input())

    T = [Node(-1, -1, -1, -1, -1) for i in range(n)]
    D = [0 for i in range(n)]
    H = [0 for i in range(n)]

    for i in range(n):
        node_id, left, right = map(int, input().split())

        if left != -1 and right != -1:
            degree = 2
        elif left == -1 and right == -1:
            degree = 0
        else:
            degree = 1

        T[node_id].left = left
        T[node_id].right = right
        T[node_id].degree = degree

        if left != -1 and right != -1:
            T[left].sibling = right
            T[right].sibling = left

        if left != -1:
            T[left].parent = node_id
        if right != -1:
            T[right].parent = node_id

    for i in range(len(T)):

        if T[i].parent == -1:
            node_type = "root"
        elif T[i].left == -1 and T[i].right == -1:
            node_type = "leaf"
        else:
            node_type = "internal node"

        print("node {0}: parent = {1}, sibling = {2}, degree = {3}, depth = {4}, height = {5}, {6}".format(i, T[i].parent, T[i].sibling, T[i].degree, GetDepth(T, i), GetHight(T, i, 0), node_type))

Main()
