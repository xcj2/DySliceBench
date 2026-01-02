import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
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
    a = [LI() + [_] for _ in range(n)]
    r = 0
    la = sorted(a,key=lambda x: [-x[0],-x[0]])
    ra = sorted(a,key=lambda x: [x[1],x[0]])
    u = set()
    li = 0
    ri = 0
    tr = 0
    c = 0
    for i in range(len(a)//2 + len(a) % 2):
        while li < n and la[li][2] in u:
            li += 1
        if c < la[li][0]:
            tr += la[li][0] - c
            c = la[li][0]
        u.add(la[li][2])

        while ri < n and ra[ri][2] in u:
            ri += 1
        if ri == n:
            break
        if c > ra[ri][1]:
            tr += c - ra[ri][1]
            c = ra[ri][1]
        u.add(ra[ri][2])

    r = tr + abs(c)
    u = set()
    li = 0
    ri = 0
    tr = 0
    c = 0
    for i in range(len(a)//2 + len(a) % 2):
        while ri < n and ra[ri][2] in u:
            ri += 1
        if c > ra[ri][1]:
            tr += c - ra[ri][1]
            c = ra[ri][1]
        u.add(ra[ri][2])

        while li < n and la[li][2] in u:
            li += 1
        if li == n:
            break
        if c < la[li][0]:
            tr += la[li][0] - c
            c = la[li][0]
        u.add(la[li][2])
    if tr + abs(c) > r:
        r = tr + abs(c)

    return r


print(main())

