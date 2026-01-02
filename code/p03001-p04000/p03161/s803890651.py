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
    n,k = LI()
    a = LI()
    r = [0] * n
    for i in range(1,n):
        ai = a[i]
        t = r[i-1] + abs(a[i-1]-ai)
        mj = i - k
        if mj < 0:
            mj = 0
        for j in range(mj,i-1):
            u = r[j] + abs(a[j]-ai)
            if t > u:
                t = u

        r[i] = t

    return r[-1]


print(main())
