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
    a = [[0,0,0]] + sorted([LI() for _ in range(n)])
    for i in range(n):
        t1,x1,y1 = a[i]
        t2,x2,y2 = a[i+1]
        sa = abs(x1-x2) + abs(y1-y2)
        ts = t2 - t1
        if ts < sa or (ts+sa) % 2 == 1:
            return 'No'

    return 'Yes'

print(main())


