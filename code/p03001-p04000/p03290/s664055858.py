import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)


def main():
    d,g = LI()
    p = []
    c = []
    for _ in range(d):
        t = LI()
        p.append(t[0])
        c.append(t[1])

    r = inf
    for i in range(2**d):
        tg = 0
        tr = 0
        for j in range(d):
            if 2**j & i:
                tg += c[j]
                tg += (j+1) * p[j] * 100
                tr += p[j]
        for j in range(d-1,-1,-1):
            if tg >= g:
                break
            if 2**j & i:
                continue
            ng = g - tg
            k = ng // ((j+1) * 100)
            if ng % ((j+1) * 100) > 0:
                k += 1
            if p[j] >= k:
                tr += k
                break
            tr += p[j]
            tg += p[j] * (j+1) * 100
        if r > tr:
            r = tr
    return r


print(main())
