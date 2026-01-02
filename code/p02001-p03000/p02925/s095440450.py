import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,copy,functools
import time

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
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

def main():
    n = I()
    a = [LI_() for _ in range(n)]
    r = 0
    c = collections.defaultdict(int)
    q = list(range(n))
    t = [0] * n
    while q:
        r += 1
        nq = []
        for i in q:
            j = a[i][t[i]]
            k = i
            if k < j:
                j,k = k,j
            c[(j,k)] += 1
            if c[(j,k)] == 2:
                t[j] += 1
                t[k] += 1
                if t[j] < n-1:
                    nq.append(j)
                if t[k] < n-1:
                    nq.append(k)
        q = nq

    for tt in t:
        if tt != n-1:
            return -1

    return r


print(main())

