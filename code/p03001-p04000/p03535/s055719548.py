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
    i = 0
    b = [0]
    for c,i in zip(a,range(n)):
        if i % 2 == 0:
            b.append(c)
        else:
            b.append(24-c)
    b.sort()
    r = a[0]
    for i in range(n):
        if b[i+1] - b[i] < r:
            r = b[i+1] - b[i]

    return r



print(main())


