import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 998244353

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)


def main():
    n,c = LI()
    d = [LI() for _ in range(c)]
    e = [LI() for _ in range(n)]
    a = [[0]*c for _ in range(3)]
    for i in range(n):
        for j in range(n):
            t = (i+j) % 3
            for k in range(c):
                a[t][k] += d[e[i][j]-1][k]
    r = inf
    for i in range(c):
        for j in range(c):
            if i == j:
                continue
            for k in range(c):
                if i == k or j == k:
                    continue
                tr = a[0][i] + a[1][j] + a[2][k]
                if r > tr:
                    r = tr

    return r


print(main())

