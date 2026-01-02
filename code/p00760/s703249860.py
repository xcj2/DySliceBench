import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**3
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
    rr = []
    n = I()
    a = [LI() for _ in range(n)]

    def f(y,m,d):
        t = (y-1) * 195
        t += (y-1) // 3 * 5
        t += (m-1) * 20
        if y % 3 > 0:
            t -= (m-1) // 2
        t += d - 1
        return t

    t = f(1000,1,1)
    for y,m,d in a:
        k = f(y,m,d)
        rr.append(t - k)

    return '\n'.join(map(str, rr))


print(main())


