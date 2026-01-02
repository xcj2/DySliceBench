import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**13
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
    h,w,k = LI()
    t = [1, 1, 2, 3, 5, 8, 13, 21]
    a = [0] * w
    a[0] = 1
    for i in range(h):
        n = [0] * w
        for j in range(w):
            n[j] = a[j] * t[j] * t[w-j-1] % mod
        for j in range(w-1):
            lr = t[j] * t[w-j-2]
            n[j] += a[j+1] * lr % mod
            n[j+1] += a[j] * lr % mod
        a = n

    return a[k-1] % mod


print(main())
