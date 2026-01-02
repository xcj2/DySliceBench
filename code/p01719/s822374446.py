import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(0,-1),(1,0),(0,1),(-1,0)]
ddn = [(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,-1),(-1,0),(-1,1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)


def main():
    rr = []

    while True:
        n,d,x = LI()
        a = [LI() for _ in range(d)]
        for i in range(d-1):
            t = [0] * (x+1)
            t[x] = x
            for j in range(n):
                if a[i][j] >= a[i+1][j]:
                    continue
                aj = a[i][j]
                ak = a[i+1][j] - aj
                for k in range(x,aj-1,-1):
                    if t[k-aj] < t[k] + ak:
                        t[k-aj] = t[k] + ak
            x = max(t)

        rr.append(x)
        break

    return '\n'.join(map(str,rr))


print(main())


