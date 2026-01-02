NIL = -1


class Node():
    def __init__(self, p, l, r):
        self.p = p
        self.l = l
        self.r = r
        self.s = NIL
        self.deg = NIL
        self.dep = NIL
        self.h = NIL


def set_attr(u):
    def set_height(u_):
        h1 = 0
        h2 = 0
        if T[u_].l != NIL:
            h1 = set_height(T[u_].l) + 1
        if T[u_].r != NIL:
            h2 = set_height(T[u_].r) + 1
        res = h1 if h1 > h2 else h2
        T[u_].h = res
        return res

    def set_depth(u_, d):
        if u_ == NIL:
            return
        T[u_].dep = d
        set_depth(T[u_].l, d + 1)
        set_depth(T[u_].r, d + 1)

    set_height(u)
    set_depth(u, 0)


N = int(input())
T = [Node(NIL, NIL, NIL) for _ in range(N)]
for _ in range(N):
    n, l, r = map(int, input().split())
    T[n].l = l
    T[n].r = r
    deg = 0
    if l != NIL:
        T[l].p = n
        deg += 1
    if r != NIL:
        T[r].p = n
        deg += 1
    if l != NIL and r != NIL:
        T[r].s = l
        T[l].s = r
    T[n].deg = deg
root = 0
for n, t in enumerate(T):
    if t.p == NIL:
        root = n
set_attr(root)
for n, t in enumerate(T):
    if t.p == NIL:
        type_ = 'root'
    elif t.l == NIL and t.r == NIL:
        type_ = 'leaf'
    else:
        type_ = 'internal node'
    print('node {}: parent = {}, sibling = {}, degree = {}, depth = {}, '
          'height = {}, {}'.format(n, t.p, t.s, t.deg, t.dep, t.h, type_))

