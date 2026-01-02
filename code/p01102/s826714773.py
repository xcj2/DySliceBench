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


def main():
    rr = []

    def f(s,t):
        if s == t:
            return 'IDENTICAL'
        sa = s.split('"')
        ta = t.split('"')
        if len(sa) != len(ta):
            return 'DIFFERENT'
        ef = False
        for i in range(len(sa)):
            si = sa[i]
            ti = ta[i]
            if si == ti:
                continue
            if i % 2 == 0 or ef:
                return 'DIFFERENT'
            ef = True
        return 'CLOSE'

    while 1:
        n = S()
        if n == '.':
            break
        rr.append(f(n,S()))

    return '\n'.join(map(str,rr))


print(main())

