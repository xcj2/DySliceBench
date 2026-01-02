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
    n,k = LI()
    a = LI()

    x = collections.defaultdict(int)
    t = [0] * n
    for i in range(n-1,-1,-1):
        t[i] = x[a[i]]
        x[a[i]] = i

    for i in range(n-1,-1,-1):
        t[i] = x[a[i]]
        x[a[i]] = i

    e = n * k
    ei = 0
    i = 0
    while ei < e - n*2:
        j = t[i]
        if j <= i:
            ei += j - i + n + 1
        else:
            ei += j - i + 1
        i = (j + 1) % n
        if i % n == 0:
            ei = e // ei * ei

    r = [0] * n
    ri = 0
    b = {}
    while ei < e:
        c = a[ei%n]
        ei += 1
        if c in b and b[c] < ri and r[b[c]] == c:
            ri = b[c]
            del b[c]
        else:
            r[ri] = c
            b[c] = ri
            ri += 1


    return JA(r[:ri], " ")

print(main())



