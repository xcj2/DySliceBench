N,M,K=map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(M)]
CD = [tuple(map(int, input().split())) for _ in range(K)]

def root(x,P):
    l = []
    n = x
    p = P[n]
    while p >= 0:
        l.append(n)
        n = p
        p = P[p]
    for a in l: P[a] = n
    return n

def same(a, b, P): return root(a,P) == root(b,P)

def count(x,P): return -P[root(x,P)]

def unite(a, b, P):
    if count(a,P) < count(b,P): a, b = b, a
    ar = root(a,P)
    br = root(b,P)
    if ar == br: return
    P[ar] += P[br]
    P[br] = ar

Fu = [-1] * N
F = [set() for _ in range(N)]
B = [set() for _ in range(N)]

for a,b in AB:
    a, b = a-1, b-1
    unite(a,b,Fu)
    F[a].add(b)
    F[b].add(a)
for c,d in CD:
    c, d = c-1, d-1
    B[c].add(d)
    B[d].add(c)

for i in range(N):
    block = 0
    for b in B[i]:
        if same(i,b,Fu): block += 1
    print(count(i,Fu) - len(F[i]) - block - 1, end=' ')