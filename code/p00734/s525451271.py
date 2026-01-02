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
    while True:
        n,m = LI()
        if n == 0:
            break

        a = [I() for _ in range(n)]
        b = [I() for _ in range(m)]
        sa = sum(a)
        sb = sum(b)
        r = -1
        for ai in sorted(a, reverse=True):
            for bi in sorted(b, reverse=True):
                if sa - ai + bi == sb - bi + ai:
                    r = '{} {}'.format(ai, bi)
                    break
        rr.append(r)

    return '\n'.join(map(str, rr))


print(main())


