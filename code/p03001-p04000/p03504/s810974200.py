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
    n,c = LI()
    a = [-1] * (c+1)
    b = sorted([LI() for _ in range(n)])
    for s,t,d in b:
        for i in range(c):
            if a[i] < s:
                a[i] = t
                break

    for i in range(c+1):
        if a[i] < 0:
            return i

    return -1



print(main())


