import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,copy,functools
import time,random

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
def JA(a, sep): return sep.join(map(str, a))
def JAA(a, s, t): return s.join(t.join(map(str, b)) for b in a)

def ff(n,k,p):
    s = set()
    for i in range(n-k+1):
        t = tuple(p[:i] + sorted(p[i:i+k]) + p[i+k:])
        s.add(t)

    return len(s)

def main():
    n,k = LI()
    p = LI()
    qc = [None] * n
    for i in range(n-1):
        if p[i] > p[i+1]:
            qc[i+1] = True

    ec = -1
    iq = []
    aq = []
    for i in range(k):
        if qc[i]:
            ec = i
        heapq.heappush(iq,p[i])
        heapq.heappush(aq,-p[i])


    r = 0
    if ec > 0:
        r += 1
    s = set()
    for i in range(k,n):
        if qc[i]:
            ec = i
        t = p[i]
        u = p[i-k]
        heapq.heappush(iq,t)
        while iq[0] in s:
            heapq.heappop(iq)
        while -aq[0] in s:
            heapq.heappop(aq)
        heapq.heappush(aq,-t)
        if iq[0] != u or aq[0] != -t:
            if ec > i - k + 1:
                r += 1
        s.add(u)

    rr = 0
    c = 1
    for i in range(1,n):
        if p[i] > p[i-1]:
            c += 1
            if c >= k:
                rr = 1
                break
        else:
            c = 1

    return r + rr


print(main())

