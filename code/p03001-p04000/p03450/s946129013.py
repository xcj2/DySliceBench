N, M = map(int, input().split())
P = [i for i in range(N)]
D = [0] * N
C = [1] * N

def par(a):
    if a == P[a]:
        return a
    p = par(P[a])
    d = D[P[a]]
    P[a] = p
    D[a] += d
    return p

def dist(a, b):
    pa = par(a)
    pb = par(b)
    if pa == pb:
        return D[b] - D[a]
    return 1 << 30

def unite(a, b, d):
    if par(a) == par(b):
        return
    if C[P[a]] < C[P[b]]:
        a, b, d = b, a, -d
    C[P[a]] += C[P[b]]
    D[P[b]] = D[a] + d - D[b]
    P[P[b]] = P[a]

for _ in range(M):
    l, r, d = map(int, input().split())
    l, r = l-1, r-1
    dd = dist(l, r)
    if dd == 1<<30:
        unite(l, r, d)
    else:
        if d != dd:
            print("No")
            break
else:
    print("Yes")