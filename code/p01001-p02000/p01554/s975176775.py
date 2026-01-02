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
    a = [S() for _ in range(n)]
    m = I()
    b = [S() for _ in range(m)]
    d = 1
    for c in b:
        if c not in a:
            rr.append('Unknown {}'.format(c))
        elif d == 1:
            rr.append('Opened by {}'.format(c))
            d = 0
        else:
            rr.append('Closed by {}'.format(c))
            d = 1

    return '\n'.join(map(str, rr))


print(main())


