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
    n,k = LI()
    xs = set()
    ys = set()
    a = []
    for _ in range(n):
        x,y = LI_()
        a.append((x,y))
        xs.add(x)
        ys.add(y)
    xd = {}
    yd = {}
    for x,i in zip(sorted(list(xs)), range(n)):
        xd[x] = i
    for y,i in zip(sorted(list(ys)), range(n)):
        yd[y] = i
    xis = sorted(list(xs))
    yis = sorted(list(ys))

    b = []
    for x,y in a:
        b.append((xd[x],yd[y]))

    if k == 1:
        return 0

    r = inf
    for i in range(n):
        xi = xis[i]
        for j in range(n-1,i-1,-1):
            xj = xis[j]
            xf = True
            for l in range(n):
                yl = yis[l]
                for m in range(n-1,l-1,-1):
                    t = 0
                    for x,y in b:
                        if i <= x <= j and l <= y <= m:
                            t += 1
                    if t >= k:
                        tr = (xj-xi) * (yis[m]-yl)
                        if tr < r:
                            r = tr
                        xf = False
                    else:
                        break
            if xf:
                break

    return r


print(main())


