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


# 豎守畑迚・ edge縺ｯN*N縺ｮ2谺｡蜈・・蛻・ cap縺ｧ騾溘￥縺ｪ縺｣縺・
class Flow():
    def __init__(self, e, N):
        self.E = e
        self.N = N

    def max_flow(self, s, t):
        r = 0
        e = self.E

        def f(c, cap):
            v = self.v
            v[c] = 1
            if c == t:
                return cap
            for i in range(self.N):
                if v[i] or e[c][i] <= 0:
                    continue
                cp = min(cap, e[c][i])
                k = f(i, cp)
                if k > 0:
                    e[c][i] -= k
                    e[i][c] += k
                    return k
            return 0

        while True:
            self.v = [None] * self.N
            fs = f(s, inf)
            if fs == 0:
                break
            r += fs

        return r

def main():
    n,m = LI()
    aa = [LI() for _ in range(m)]

    e = [[0] * n for _ in range(n)]
    for a,b,c in aa:
        e[a][b] = c

    fl = Flow(e, n)
    r = fl.max_flow(0, n-1)

    return r

# start = time.time()
print(main())
# pe(time.time() - start)




