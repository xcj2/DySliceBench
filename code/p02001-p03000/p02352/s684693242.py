import sys,queue,math,copy,itertools,bisect
sys.setrecursionlimit(10**7)
INF = 10**10
LI = lambda : [int(x) for x in sys.stdin.readline().split()]
_LI = lambda : [int(x)-1 for x in sys.stdin.readline().split()]
NI = lambda : int(sys.stdin.readline())

N,Q = LI()
N0 = 2 ** (N.bit_length())
node = [0 for _ in range(N0*2)]
lazy = [0 for _ in range(N0*2)]


def gindex(l,r):
    L = l + N0; R = r + N0
    lm = (L // (L & -L)) // 2
    rm = (R // (R & -R)) // 2
    while L < R:
        if R <= rm:
            yield R-1
        if L <= lm:
            yield L-1
        L //= 2; R //= 2
    while L > 0:
        yield L-1
        L //= 2

def eval(*ids):
    for i in reversed(ids):
        v = lazy[i]
        if v:
            lazy[i*2+1] += v
            lazy[i*2+2] += v
            node[i*2+1] += v
            node[i*2+2] += v
        lazy[i] = 0

def data_add(l,r,v):
    *ids, = gindex(l,r)
    eval(*ids)

    L = l + N0; R = r + N0
    while L < R:
        if R % 2:
            R -= 1
            lazy[R-1] += v
            node[R-1] += v
        if L % 2:
            lazy[L-1] += v
            node[L-1] += v
            L += 1
        L //= 2; R //= 2

    for i in ids:
        node[i] = min(node[i*2+1],node[i*2+2])

def data_get(l,r):
    eval(*gindex(l,r))

    ret = INF
    L = l + N0; R = r + N0
    while L < R:
        if R % 2:
            R -= 1
            ret = min(ret,node[R-1])
        if L % 2:
            ret = min(ret,node[L-1])
            L += 1
        L //= 2; R //= 2
    return ret

for _ in range(Q):
    s = LI()
    if s[0] == 0:
        data_add(s[1],s[2]+1,s[3])
    else:
        print (data_get(s[1],s[2]+1))


