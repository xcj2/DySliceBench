NIL = -1


class Node:
    right = NIL
    left = NIL
    parent = NIL


def setHeight(u):
    global T, H
    hr = 0
    hl = 0
    if T[u].right != NIL:
        hr = setHeight(T[u].right) + 1
    if T[u].left != NIL:
        hl = setHeight(T[u].left) + 1
    h = max(hr, hl)
    H[u] = h
    return h


def setDepth(u, d):
    global T, D
    D[u] = d
    if T[u].right != NIL:
        setDepth(T[u].right, d + 1)
    if T[u].left != NIL:
        setDepth(T[u].left, d + 1)


def getSibling(u):
    global T
    if T[u].parent == NIL:
        return NIL
    if T[T[u].parent].left != u and T[T[u].parent].left != NIL:
        return T[T[u].parent].left
    if T[T[u].parent].right != u and T[T[u].parent].right != NIL:
        return T[T[u].parent].right
    return NIL


def getDegree(u):
    global T
    deg = 0
    if T[u].left != NIL: deg += 1
    if T[u].right != NIL: deg += 1
    return deg


def show_info(u):
    global T, D, H
    label = ""
    if T[u].parent == NIL:
        label = 'root'
    elif T[u].left == NIL and T[u].right == NIL:
        label = 'leaf'
    else:
        label = 'internal node'
    print("node {0}: parent = {1}, sibling = {2}, degree = {3}, depth = {4}, height = {5}, {6}".format(u, T[u].parent,
                                                                                                       getSibling(u),
                                                                                                       getDegree(u),
                                                                                                       D[u],
                                                                                                       H[u], label))


if __name__ == "__main__":
    # ????????¨??????
    n = int(input())
    T, D, H = [], [], []
    root_num = NIL
    for i in range(n):
        T.append(Node())
        D.append(NIL)
        H.append(0)
    for i in range(n):
        id, r, l = map(int, input().split())
        T[id].right = r
        T[id].left = l
    for i in range(n):
        if T[i].right != NIL:
            T[T[i].right].parent = i
        if T[i].left != NIL:
            T[T[i].left].parent = i
    for i in range(n):
        if T[i].parent == NIL:
            root_num = i

    setHeight(root_num)
    setDepth(root_num, 0)
    for i in range(n):
        show_info(i)