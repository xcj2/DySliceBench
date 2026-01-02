class Vertex:
    def __init__(self, p):
        self.p = p
        self.r = 0


class Edge:
    def __init__(self, s, t, w):
        self.s = s
        self.t = t
        self.w = w


def union(x, y):
    x = findSet(x)
    y = findSet(y)
    link(x, y)


def link(x, y):
    if V[x].r > V[y].r:
        V[y].p = x

    else:
        V[x].p = y
        if V[x].r == V[y].r: V[y].r = V[y].r + 1


def findSet(x):
    if x != V[x].p:
        V[x].p = findSet(V[x].p)

    return V[x].p


def same(x, y):
    return findSet(x) == findSet(y)



if __name__ == '__main__':
    n_V, n_E = map(int, input().split())

    #
    V = []
    for i in range(n_V):
        V.append(Vertex(i))

    #
    E = []
    for _ in range(n_E):
        s, t, w = map(int, input().split())
        E.append(Edge(s, t, w))

    #
    E.sort(key=lambda e : e.w)

    #
    sum_w = 0
    for e in E:
        if not same(e.s, e.t):
            union(e.s, e.t)
            sum_w += e.w

    print(sum_w)

