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


def main():
    n = I()
    sa = [S() for _ in range(n)]
    e = collections.defaultdict(set)
    for i in range(n):
        s = sa[i]
        for j in range(i+1,n):
            if s[j] == '1':
                e[i].add(j)
                e[j].add(i)

    r = -1
    for i in range(n):
        k = 1
        a = [set(), set([i])]
        u = set([i])
        while len(u) < n:
            k += 1
            v = set()
            for c in a[k-1]:
                v |= e[c]
            v -= a[k-2]
            if len(v & u) > 0:
                k = -1
                break
            vv = set()
            for c in v:
                vv |= e[c]
            if len(vv & v) > 0:
                k = -1
                break
            a.append(v)
            u |= v
        if r < k:
            r = k

    return r


print(main())



