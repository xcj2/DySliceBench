import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,copy,functools
import time,random

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
mod2 = 998244353
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
def JA(a, sep): return sep.join(map(str, a))
def JAA(a, s, t): return s.join(t.join(map(str, b)) for b in a)


def main():
    s = S()
    a = []
    t = s[0]
    u = 1
    for c in s[1:]:
        if t == c:
            u += 1
        else:
            t = c
            a.append(u)
            u = 1
    a.append(u)
    f = False
    r = 0
    for c in a:
        if f:
            r += 1
            c -= 1
        f = False
        if c == 0:
            continue
        if c == 1:
            r += 1
            continue
        if c == 2:
            r += 1
            f = True
            continue
        r += c // 3 * 2
        if c % 3 > 0:
            r += 1
        if c % 3 == 2:
            f = True

    return r


print(main())



