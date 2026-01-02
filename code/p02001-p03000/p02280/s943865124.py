import sys


def dep(u, p):
    depth[u] = p
    if TREE[u][1] != NIL:
        dep(TREE[u][1], p+1)
    if TREE[u][2] != NIL:
        dep(TREE[u][2], p+1)


def hei(u):
    h1, h2 = 0, 0
    if TREE[u][1] != NIL:
        h1 = hei(TREE[u][1]) + 1
    if TREE[u][2] != NIL:
        h2 = hei(TREE[u][2]) + 1
    height[u] = max(h1, h2)
    return height[u]


def print_ans():
    for i in range(n):
        print("node {}: parent = {}, sibling = {}, degree = {}, depth = {}, height = {}, {}"
              .format(i, TREE[i][0], TREE[i][3],
                      2 if TREE[i][1] != -1 and TREE[i][2] != -1 else 0 if TREE[i][1] == NIL and TREE[i][2] == NIL else 1,
                      depth[i], height[i],
                      "root" if TREE[i][0] == NIL else "leaf" if TREE[i][1] == NIL and TREE[i][2] == NIL else "internal node"))


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    NIL = -1
    TREE = [[NIL, NIL, NIL, NIL] for i in range(n)]
    depth = [-1 for i in range(n)]
    height = [-1 for i in range(n)]
    root = set(range(n))
    for inp in sys.stdin.readlines():
        inp = list(map(int, inp.split()))
        if inp[1] != -1:
            TREE[inp[0]][1] = inp[1]
            TREE[inp[1]][0] = inp[0]
            TREE[inp[1]][3] = inp[2]
        if inp[2] != -1:
            TREE[inp[0]][2] = inp[2]
            TREE[inp[2]][0] = inp[0]
            TREE[inp[2]][3] = inp[1]
        root -= set([inp[1], inp[2]])
    a = root.pop()
    dep(a, 0)
    hei(a)
    print_ans()