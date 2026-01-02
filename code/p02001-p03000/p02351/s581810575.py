import sys,queue,math,copy,itertools,bisect
LI = lambda : [int(x) for x in sys.stdin.readline().split()]
_LI = lambda : [int(x)-1 for x in sys.stdin.readline().split()]
NI = lambda : int(sys.stdin.readline())

N,Q = LI()
N0 = 2 ** (N).bit_length()
data = [0 for _ in range(N0*2)]
lazy = [0 for _ in range(N0*2)]

def gindex(l, r):
    L = l + N0; R = r + N0
    lm = (L // (L & -L)) // 2
    rm = (R // (R & -R)) // 2
    while L < R:
        if R <= rm:
            yield R-1
        if L <= lm:
            yield L-1
        L //= 2; R //= 2
    while L:
        yield L-1
        L //= 2

def eval(*ids):
    for i in reversed(ids):
        v = lazy[i]
        if v == 0: continue
        lazy[i*2+1] += v // 2
        lazy[i*2+2] += v // 2
        data[i*2+1] += v // 2
        data[i*2+2] += v // 2

        lazy[i] = 0

def data_add(l,r,x):
    *ids, = gindex(l,r)
    eval(*ids)
    L = l + N0; R = r + N0
    n = 1
    while L < R:
        if R % 2:
            R -= 1
            lazy[R-1] += x * n
            data[R-1] += x * n
        if L % 2:
            lazy[L-1] += x * n
            data[L-1] += x * n
            L += 1
        L //= 2; R //= 2; n *= 2
    for i in ids:
        data[i] = data[i*2+1] + data[i*2+2]

def data_get(l,r):
    eval(*gindex(l,r))
    L = l + N0; R = r + N0

    ret = 0
    while L < R:
        if R % 2:
            R -= 1
            ret += data[R-1]
        if L % 2:
            ret += data[L-1]
            L += 1
        L //= 2; R //= 2
    return ret

for _ in range(Q):
    q = LI()
    if q[0] == 0:
        data_add(q[1],q[2]+1,q[3])
    else:
        print (data_get(q[1],q[2]+1))
