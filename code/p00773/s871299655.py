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

    def f(n,p):
        return n * (100+p) // 100

    while True:
        x,y,s = LI()
        if x == 0:
            break
        a = set()
        m = -1
        for i in range(1,s):
            for j in range(i,s):
                u = f(i,x) + f(j,x)
                if u > s:
                    break
                if u == s:
                    t = f(i,y) + f(j,y)
                    if m < t:
                        m = t
        rr.append(m)

    return '\n'.join(map(str, rr))


print(main())


