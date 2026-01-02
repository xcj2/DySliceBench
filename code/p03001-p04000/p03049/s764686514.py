import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,copy,functools
import random

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(): return [list(map(int, l.split())) for l in sys.stdin.readlines()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)
def pe(s): return print(str(s), file=sys.stderr)


def main():
    n = I()
    a = [S() for _ in range(n)]
    ss = '-'
    r = 0
    ba = []
    ta = []
    tb = []
    for s in a:
        if s[0] == 'B':
            if s[-1] == 'A':
                ba.append(s)
            else:
                tb.append(s)
        elif s[-1] == 'A':
            ta.append(s)
        else:
            r += len(s.split('AB')) - 1

    while ba or ta or tb:
        if ss[-1] == 'A':
            if ba:
                ss += ba[-1]
                ba = ba[:-1]
            elif tb:
                ss += tb[-1]
                tb = tb[:-1]
            else:
                ss += ta[-1]
                ta = ta[:-1]
        else:
            if ta:
                ss += ta[-1]
                ta = ta[:-1]
            elif ba:
                ss += ba[-1]
                ba = ba[:-1]
            else:
                ss += tb[-1]
                tb = tb[:-1]
    # print(r,ss)

    return r + len(ss.split('AB')) - 1


print(main())


