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
    n = I()
    a = sorted([I() for _ in range(n)])
    if n % 2 == 0:
        k = n // 2
        b = a[:k-1]
        c = a[k+1:]
        t = [0] * n
        t[0] = a[k]
        t[-1] = a[k-1]
        for i in range(k-1):
            t[i*2+1] = b[i]
            t[i*2+2] = c[i]
        r = 0
        for i in range(n-1):
            r += abs(t[i]-t[i+1])

        return r

    k = n // 2 + 1
    b = a[:k-1]
    c = a[k+1:]
    t = [0] * n
    t[0] = a[k]
    t[-1] = a[k-1]
    t[-2] = b[-1]
    for i in range(k-2):
        t[i*2+1] = b[i]
        t[i*2+2] = c[i]
    r = 0
    for i in range(n-1):
        r += abs(t[i]-t[i+1])

    b = a[:k-2]
    c = a[k:]
    t = [0] * n
    t[0] = a[k-1]
    t[-1] = a[k-2]
    t[-2] = c[-1]
    for i in range(k-2):
        t[i*2+1] = c[i]
        t[i*2+2] = b[i]
    tr = 0
    for i in range(n-1):
        tr += abs(t[i]-t[i+1])

    if r < tr:
        r = tr

    return r


print(main())
