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

# 下がtrue, falseになる最小値を返す
def bs(f, mi, ma):
    mm = -1
    while ma > mi:
        mm = (ma+mi) // 2
        if f(mm):
            mi = mm + 1
        else:
            ma = mm
    if f(mm):
        return mm + 1
    return mm

def main():
    n = I()
    a = LI()

    def f(i):
        for c in a:
            i -= i%c
        return i < 2

    def g(i):
        for c in a:
            i -= i%c
        return i <= 2

    mi = bs(f,0,sum(a)+3)
    ma = bs(g,0,sum(a)+3) - 1
    if mi <= ma:
        return '{} {}'.format(mi,ma)
    return -1




print(main())


