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
    l = k + 1

    y = [1] * (a[-1]+1) + [0] * (l-a[-1]-1)

    for i in range(n-2,-1,-1):
        z = [None] * l
        s = 0
        c = a[i] + 1
        for j in range(c):
            z[j] = s = (s + y[j]) % mod

        for j in range(c,l):
            z[j] = s = (s + y[j] - y[j-c]) % mod

        y = z

    return (y[-1] + mod) % mod


print(main())
