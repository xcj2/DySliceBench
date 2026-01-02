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
    n,w = LI()
    aa = sorted([LI() for _ in range(n)])
    u = sum(map(lambda x: x[1], aa))
    r = [inf] * (u+1)
    r[0] = 0
    mx = 0
    for a,b in aa:
        mx += b
        for i in range(min(mx, u-b),-1,-1):
            if r[i+b] > a + r[i]:
                r[i+b] = a + r[i]

    for i in range(u,0,-1):
        if r[i] <= w:
            return i

    return 0


print(main())
