import sys
readline = sys.stdin.readline

N, M = map(int, readline().split())
L = [[] for i in range(N+1)]
R = [[] for i in range(N+1)]
for i in range(M):
    l, r, a = map(int, readline().split())
    L[l-1].append((r, a))

INF = 2**31-1

LV = (N).bit_length()
N0 = 2**LV
data = [0]*(2*N0)
lazy = [0]*(2*N0)

I = []; J = []
for x in range(N0+1):
    y = N0 + x
    z = (y // (y & -y)) >> 1
    J.append(2*z-1 if z else 0)
    r = []
    while z:
        r.append(z)
        z >>= 1
    r.reverse()
    I.append(r)
I.append([])

def propagates(ids):
    for i in ids:
        v = lazy[i-1]
        if not v:
            continue
        lazy[2*i-1] += v; lazy[2*i] += v
        data[2*i-1] += v; data[2*i] += v
        lazy[i-1] = 0

# update [0, r)
def update(r, x):
    #propagates(I[r])

    i = r
    while i:
        v = J[i]
        lazy[v] += x; data[v] += x
        i -= (i & -i)

    k = (J[r] + 1) >> 1
    while k:
        data[k-1] = max(data[2*k-1], data[2*k]) + lazy[k-1]
        k >>= 1

# update[k, k+1)
def update1(k, x):
    #propagates(I[k])
    k += N0
    data[k-1] += x
    while k:
        k >>= 1
        data[k-1] = max(data[2*k-1], data[2*k]) + lazy[k-1]


# query [0, r)
def query(r):
    return max(map(data.__getitem__, qquery(r)))

def qquery(r):
    propagates(I[r])

    while r:
        yield J[r]
        r -= (r & -r)

# query [k, k+1)
def query1(k, x):
    propagates(I[k])
    return data[k + N0 - 1]


for i in range(N):
    for r, a in L[i]:
        update(i+1, a)
        R[r].append((i, a))
    for l, a in R[i]:
        update(l+1, -a)
    v = query(i+1)
    update1(i+1, v)
for l, a in R[N]:
    update(l+1, -a)
sys.stdout.write("%d\n" % query(N+1))