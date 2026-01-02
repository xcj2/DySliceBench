import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 998244353

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)


def main():
    rr = []

    while True:
        n,w,h = LI()
        a = [LI() for _ in range(n)]
        b = []
        c = []
        for x,y,ww in a:
            b.append((x-ww,x+ww))
            c.append((y-ww,y+ww))
        b.sort()
        c.sort()
        f = False
        mi = b[0][0]
        ma = b[0][1]
        for l,r in b[1:]:
            if l > ma:
                break
            ma = max(r,ma)
        if mi <= 0 and ma >= w:
            f = True
        mi = c[0][0]
        ma = c[0][1]
        for l,r in c[1:]:
            if l > ma:
                break
            ma = max(r,ma)
        if mi <= 0 and ma >= h:
            f = True

        if f:
            rr.append('Yes')
        else:
            rr.append('No')
        break

    return '\n'.join(map(str, rr))


print(main())


