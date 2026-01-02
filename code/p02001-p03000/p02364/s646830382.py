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
    if r[x] > r[y]:
        p[y] = x

    else:
        p[x] = y
        if r[x] == r[y]: r[y] = r[y] + 1


def findSet(x):
    if x != p[x]:
        p[x] = findSet(p[x])

    return p[x]


def same(x, y):
    return findSet(x) == findSet(y)



if __name__ == '__main__':
    p, r = [], []

    n_V, n_E = map(int, input().split())

    for i in range(n_V):
        p.append(i)
        r.append(0)

    Es = []
    for _ in range(n_E):
        s, t, w = map(int, input().split())
        Es.append(Edge(s, t, w))

    Es.sort(key=lambda e : e.w)

    sum_w = 0
    for e in Es:
        if not same(e.s, e.t):
            union(e.s, e.t)
            sum_w += e.w

    print(sum_w)

