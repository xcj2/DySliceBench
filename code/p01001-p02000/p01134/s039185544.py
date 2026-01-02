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


def intersection(a1, a2, b1, b2):
    x1,y1 = a1
    x2,y2 = a2
    x3,y3 = b1
    x4,y4 = b2

    ksi = (y4 - y3) * (x4 - x1) - (x4 - x3) * (y4 - y1)
    eta = (x2 - x1) * (y4 - y1) - (y2 - y1) * (x4 - x1)
    delta = (x2 - x1) * (y4 - y3) - (y2 - y1) * (x4 - x3)
    if delta == 0:
        return None
    ramda = ksi / delta;
    mu = eta / delta;
    if ramda >= 0 and ramda <= 1 and mu >= 0 and mu <= 1:
        return (round(x1 + ramda * (x2 - x1), 9), round(y1 + ramda * (y2 - y1), 9))

    return None

def main():
    rr = []

    def f(n):
        def _f(l):
            return [(l[0],l[1]), (l[2],l[3])]
        a = [_f(LI()) for _ in range(n)]
        r = 1 + n
        itc = collections.defaultdict(int)
        for i in range(n):
            a1,a2 = a[i]
            for j in range(i+1,n):
                it = intersection(a1,a2,a[j][0],a[j][1])
                if not it:
                    continue
                if max(it) == 100 or min(it) == -100:
                    continue
                itc[it] += 1

        # print('itc',itc)

        for v in itc.values():
            if v <= 1:
                r += v
                continue
            for i in range(101):
                if v == i * (i+1) / 2:
                    r += i
                    break

        return r

    while 1:
        n = I()
        if n == 0:
            break
        rr.append(f(n))

    return '\n'.join(map(str,rr))


print(main())

