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
    h,w,n = LI()
    sc,sr = LI()
    s = S()
    t = S()
    ra = ri = 0
    ca = ci = 0
    for i in range(n-1,-1,-1):
        si = s[i]
        ti = t[i]

        if ti == 'L':
            if ra > 0:
                ra -= 1
        elif ti == 'R':
            if ri > 0:
                ri -= 1
        elif ti == 'U':
            if ca > 0:
                ca -= 1
        else:
            if ci > 0:
                ci -= 1

        if si == 'L':
            ri += 1
        elif si == 'R':
            ra += 1
        elif si == 'U':
            ci += 1
        else:
            ca += 1

        if ri + ra >= w:
            return 'NO'
        if ci + ca >= h:
            return 'NO'

        # print(ri,ra,'c',ci,ca,'s',sr,sc)

    if sr <= ri or sr + ra > w:
        return 'NO'
    if sc <= ci or sc + ca > h:
        return 'NO'

    return 'YES'


print(main())


