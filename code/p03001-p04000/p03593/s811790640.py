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

def main():
    h,w = LI()
    d = collections.defaultdict(int)
    for _ in range(h):
        for c in S():
            d[c] += 1

    t = 0
    t2 = 0
    for v in d.values():
        t += v//4
        t2 += (v%4) // 2

    f = (h//2) * (w//2)
    if t < f:
        return 'No'
    t2 += (t-f) * 2
    if w%2 == 1:
        t2 -= h//2
    if h%2 == 1:
        t2 -= w//2
    if t2 < 0:
        return 'No'
    return 'Yes'



print(main())


