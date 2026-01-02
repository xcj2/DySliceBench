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

    t = [[0]*n for _ in range(n)]
    for i in range(n):
        t[i][i] = a[i]

    for i in range(n-2,-1,-1):
        z = t[i]
        y = t[i+1]
        for j in range(i+1,n):
            r = a[j] - z[j-1]
            u = a[i] - y[j]
            if r < u:
                r = u
            z[j] = r

    return t[0][-1]


print(main())
