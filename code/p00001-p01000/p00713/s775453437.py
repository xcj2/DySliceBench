import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**13
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


def cc(x1, y1, x2, y2):
    xd = x2 - x1
    yd = y2 - y1
    xc = (x1 + x2) / 2
    yc = (y1 + y2) / 2
    k = pow(1.0 / (xd**2 + yd**2) - 0.25, 0.5)
    xd *= k
    yd *= k
    return [[xc - yd, yc + xd], [xc + yd, yc - xd]]

def main():
    rr = []
    eps1 = 1 + eps

    def f(n):
        a = sorted([LF() for _ in range(n)])
        r = 1
        for i in range(n):
            ax, ay = a[i]
            for j in range(i+1,n):
                bx, by = a[j]
                if bx - ax > 2:
                    break
                if pow(ax-bx, 2) + pow(ay-by, 2) > 4:
                    continue
                for x, y in cc(ax, ay, bx, by):
                    t = 0
                    for k in range(n):
                        if x - a[k][0] > 1:
                            continue
                        if a[k][0] - x > 1:
                            break
                        if pow(x-a[k][0], 2) + pow(y-a[k][1], 2) < eps1:
                            t += 1
                    if r < t:
                        r = t

        return r

    while 1:
        n = I()
        if n == 0:
            break
        rr.append(f(n))

    return '\n'.join(map(str,rr))


print(main())

