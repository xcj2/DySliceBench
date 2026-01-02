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
    k = S()
    d = I()
    t = [0] * d
    c = 0
    for i in k:
        i = int(i)
        u = t[:]
        for j in range(c,c+i):
            u[j%d] += 1
        c += i
        c %= d
        d1 = max(0, d-10)
        for j in range(d1):
            for jj in range(j+1,j+10):
                u[jj] += t[j]
            u[j] %= mod

        for j in range(d1, d):
            for jj in range(j+1,j+10):
                u[jj%d] += t[j]
            u[j] %= mod
        t = u

    if c == 0:
        return t[0] % mod

    return (t[0] - 1) % mod


print(main())
