import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
gosa = 1.0 / 10**9
mod = 10**9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()


def main():
    N = I()
    a = LI()
    r = 0
    f = True
    while f:
        f = False
        for i in range(N):
            if a[i] < N:
                continue
            f = True
            t = a[i] // N
            r += t
            for j in range(N):
                if i == j:
                    continue
                a[j] += t
            a[i] -= t * N
    return r



print(main())

