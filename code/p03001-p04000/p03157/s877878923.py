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
    h,w = LI()
    a = [[c == '#' for c in S()] for _ in range(h)]
    b = [[None] * w for _ in range(h)]

    def f(i,j,k):
        if b[i][j] or a[i][j] != k:
            return (0,0)
        b[i][j] = 1
        r = [1,0]
        for di,dj in dd:
            ni = i + di
            nj = j + dj
            if ni < 0 or ni >= h or nj < 0 or nj >= w:
                continue
            res = f(ni,nj,not k)
            r[0] += res[1]
            r[1] += res[0]
        return r

    r = 0
    for i in range(h):
        for j in range(w):
            t = f(i,j,a[i][j])
            r += t[0] * t[1]

    return r



print(main())


