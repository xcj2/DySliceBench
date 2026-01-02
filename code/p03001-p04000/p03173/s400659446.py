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
    a = LI()
    l = n + 1

    t = [[0]*n for _ in range(n)]
    w = [0] * l
    for i in range(n):
        w[i+1] = w[i] + a[i]

    for i in range(n-2,-1,-1):
        z = t[i]
        y = t[i+1]
        c = w[i]
        for j in range(i+1,n):
            b = inf
            for k in range(i,j):
                e = z[k] + t[k+1][j]
                if b > e:
                    b = e
            t[i][j] = b + w[j+1] - c

    return t[0][-1]


print(main())
