import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,copy,functools
import time,random

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
mod2 = 998244353
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(): return [list(map(int, l.split())) for l in sys.stdin.readlines()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)
def pe(s): return print(str(s), file=sys.stderr)
def JA(a, sep): return sep.join(map(str, a))
def JAA(a, s, t): return s.join(t.join(map(str, b)) for b in a)

def wff(n,l,abc,st):
    nl = list(range(n))
    d = [[inf] * n for _ in nl]
    for i in nl:
        d[i][i] = 0
    for a,b,c in abc:
        a -= 1
        b -= 1
        d[a][b] = c
        d[b][a] = c

    for i in nl:
        di = d[i]
        for j in nl:
            if i == j:
                continue
            dj = d[j]
            for k in nl:
                if i != k and j != k and dj[k] > dj[i] + di[k]:
                    dj[k] = dj[i] + di[k]

    dd = [[inf] * n for _ in nl]
    for i in nl:
        dd[i][i] = 0
    for i in nl:
        for j in nl:
            if j != i and d[i][j] <= l:
                dd[i][j] = 1

    for i in nl:
        di = dd[i]
        for j in nl:
            if i == j:
                continue
            dj = dd[j]
            for k in nl:
                if i != k and j != k and dj[k] > dj[i] + di[k]:
                    dj[k] = dj[i] + di[k]

    rr = []
    for s,t in st:
        if dd[s][t] == inf:
            rr.append(-1)
        else:
            rr.append(dd[s][t] - 1)

    return JA(rr, "\n")


def main():
    n,m,l = LI()
    abc = [LI() for _ in range(m)]
    q = I()
    st = [LI_() for _ in range(q)]

    if m > 300 * 100:
        return wff(n,l,abc,st)

    e = collections.defaultdict(list)
    for a,b,c in abc:
        a -= 1
        b -= 1
        e[a].append((b, c))
        e[b].append((a, c))

    def search(s):
        d = collections.defaultdict(lambda: inf)
        d[s] = 0
        q = []
        heapq.heappush(q, (0, s))
        v = collections.defaultdict(bool)
        while len(q):
            k, u = heapq.heappop(q)
            if v[u]:
                continue
            v[u] = True

            for uv, ud in e[u]:
                if v[uv]:
                    continue
                vd = k + ud
                if d[uv] > vd and vd <= l:
                    d[uv] = vd
                    heapq.heappush(q, (vd, uv))

        return set([k for k,v in d.items() if v <= l])

    d = {}
    for i in range(n):
        d[i] = search(i)

    dd = [[inf] * n for _ in range(n)]
    for i in range(n):
        q = [(0, i)]
        qi = 0
        v = set([i])
        while len(q) > qi:
            k, t = q[qi]
            qi += 1
            u = d[t] - v
            v |= u
            dd[i][t] = k
            for w in u:
                q.append((k+1, w))

    rr = []
    for s,t in st:
        if dd[s][t] == inf:
            rr.append(-1)
        else:
            rr.append(dd[s][t] - 1)


    return JA(rr, "\n")

print(main())



