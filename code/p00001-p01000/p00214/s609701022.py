def dot3(O, A, B):
    ox, oy = O; ax, ay = A; bx, by = B
    return (ax - ox) * (bx - ox) + (ay - oy) * (by - oy)
def cross3(O, A, B):
    ox, oy = O; ax, ay = A; bx, by = B
    return (ax - ox) * (by - oy) - (bx - ox) * (ay - oy)
def dist2(A, B):
    ax, ay = A; bx, by = B
    return (ax - bx) ** 2 + (ay - by) ** 2
def is_intersection(P0, P1, Q0, Q1):
    C0 = cross3(P0, P1, Q0)
    C1 = cross3(P0, P1, Q1)
    D0 = cross3(Q0, Q1, P0)
    D1 = cross3(Q0, Q1, P1)
    if C0 == C1 == 0:
        E0 = dot3(P0, P1, Q0)
        E1 = dot3(P0, P1, Q1)
        if not E0 < E1:
            E0, E1 = E1, E0
        return E0 <= dist2(P0, P1) and 0 <= E1
    return C0 * C1 <= 0 and D0 * D1 <= 0

def contains(P, Q):
    v = []
    for q in Q:
        for i in range(4):
            v.append(cross3(P[i-1], P[i], q))
        if all(e <= 0 for e in v) or all(e >= 0 for e in v):
            return 1
    return 0

def check(Pi, Pj):
    if contains(Pi, Pj) or contains(Pj, Pi):
        return 1
    for i in range(4):
        for j in range(4):
            if is_intersection(Pi[i-1], Pi[i], Pj[j-1], Pj[j]):
                return 1
    return 0

def solve():
    M = readline(1)[0]
    *p, = range(M)
    def root(x):
        if x == p[x]:
            return x
        p[x] = y = root(p[x])
        return y
    def unite(x, y):
        px = root(x); py = root(y)
        if px < py:
            p[py] = px
        else:
            p[px] = py

    P = []
    for i in range(M):
        xa, ya, xb, yb, xc, yc, xd, yd = readline(8)
        P.append(((xa, ya), (xb, yb), (xc, yc), (xd, yd)))
    for i in range(M):
        for j in range(i+1, M):
            if check(P[i], P[j]):
                unite(i, j)
    res = 0
    for i in range(M):
        if i == root(i):
            res += 1
    return res


*r, = map(int, open(0).read().split())
it = iter(r)

def readline(v):
    r = []
    for i in range(v):
        r.append(next(it))
    return r

while 1:
    N = readline(1)[0]
    if N == 0:
        break
    for i in range(N):
        print(solve())
