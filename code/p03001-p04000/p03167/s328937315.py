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
    a = [[c for c in S()] for _ in range(h)]
    r = [[0]*w for _ in range(h)]
    r[0][0] = 1
    for i in range(h):
        for j in range(w):
            if a[i][j] == '#':
                continue
            if i > 0:
                r[i][j] += r[i-1][j]
            if j > 0:
                r[i][j] += r[i][j-1]
            r[i][j] %= mod

    return r[-1][-1]


print(main())
