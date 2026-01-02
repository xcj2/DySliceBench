import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**15
mod = 10**9+7

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
    a = sorted(LI())
    b = sorted(LI())
    c = sorted(LI())
    t = [0] * n
    j = 0
    for i in range(n):
        bi = b[i]
        while j < n and c[j] <= bi:
            j += 1
        t[i] = n - j
    r = 0
    for i in range(n-2,-1,-1):
        t[i] += t[i+1]
    j = 0
    for i in range(n):
        ai = a[i]
        while j < n and b[j] <= ai:
            j += 1
        if j < n:
            r += t[j]

    return r



print(main())


