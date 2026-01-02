import sys
input = sys.stdin.readline
N, M = map(int, input().split())

N0 = 2**((N+1).bit_length())
INF = 10**18
data = [0]*(2*N0)
lazy = [0]*(2*N0)

def gindex(l, r):
    L = l + N0; R = r + N0
    lm = (L // (L & -L)) >> 1
    rm = (R // (R & -R)) >> 1
    while L < R:
        if R <= rm:
            yield R
        if L <= lm:
            yield L
        L >>= 1; R >>= 1
    while L:
        yield L
        L >>= 1

def propagates(*ids):
    for i in reversed(ids):
        v = lazy[i-1]
        if not v:
            continue
        lazy[2*i-1] += v; lazy[2*i] += v
        data[2*i-1] += v; data[2*i] += v
        lazy[i-1] = 0
        
def update(l, r, x):
    L = N0 + l; R = N0 + r
    while L < R:
        if R & 1:
            R -= 1
            lazy[R-1] += x; data[R-1] += x
        if L & 1:
            lazy[L-1] += x; data[L-1] += x
            L += 1
        L >>= 1; R >>= 1

    for i in gindex(l, r):
        data[i-1] = max(data[2*i-1], data[2*i]) + lazy[i-1]

def update2(k, x):
    k += N0-1
    data[k] = x
    while k >= 0:
        k = (k - 1) // 2
        data[k] = max(data[2*k+1], data[2*k+2])

def query(l, r):
    propagates(*gindex(l, r))
    L = N0 + l; R = N0 + r
    s = -INF
    while L < R:
        if R & 1:
            R -= 1
            s = max(s, data[R-1])
        if L & 1:
            s = max(s, data[L-1])
            L += 1
        L >>= 1; R >>= 1
    return s

xs = [0]*(N+1)
ys = [[] for _ in range(N+1)]
for _ in range(M):
    l, r, a = map(int, input().split())
    xs[l] += a
    ys[r].append((l,a))

for i in range(1, N+1):
    update(0,i,xs[i])
    update2(i, query(0, i))
    for l, a in ys[i]:
        update(0, l, -a)
print(query(0,N+1))
