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
def M(n): return ModInt(n)
def MI(): return M(I())


def main():
    k,a,b = LI()
    if k <= a:
        return 1
    if a <= b:
        return -1
    t = a-b
    r = int((k-a) / t)
    for i in range(r-10,r+10):
        if i*t + a >= k:
            return i*2+1

    return -1



print(main())


