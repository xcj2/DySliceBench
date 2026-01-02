import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)


def main():
    n = I()
    a = [LI() for _ in range(n)]
    m = 2**n
    s = [[0] * m for _ in range(n+1)]
    s[0][0] = 1
    ii = [2**i for i in range(n)]
    for i in range(n):
        t = s[i+1]
        u = s[i]
        b = [ii[c] for c in range(n) if a[i][c]]
        for k in range(m):
            v = u[k]
            v = v % mod
            if v < 1:
                continue
            for j in b:
                if not (j & k):
                    t[k | j] += v

    return s[-1][-1] % mod


print(main())

