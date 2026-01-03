import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()


def main():
    h,w = LI()
    if h < w:
        h,w = w,h

    if h % 3 == 0 or w % 3 == 0:
        return 0

    r = inf
    if h >= 3:
        r = w
    w1 = w//2
    w2 = (w+1)//2
    for t in range(1,h):
        a = [t*w, (h-t) * w1, (h-t) * w2]
        tr = max(a) - min(a)
        if tr < r:
            r = tr
    h1 = h//2
    h2 = (h+1)//2
    for t in range(1,w):
        a = [t*h, (w-t) * h1, (w-t) * h2]
        tr = max(a) - min(a)
        if tr < r:
            r = tr
    return r



print(main())
