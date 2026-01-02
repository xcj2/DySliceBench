import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**15
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
    s = S()
    sa = ''
    for c in s:
        if c == '?':
            sa += 'a'
        else:
            sa += c
    t = S()
    r = None
    l = len(t)
    for i in range(len(s)-l+1):
        f = True
        for j in range(l):
            if s[i+j] != '?' and s[i+j] != t[j]:
                f = False
                break
        if f:
            tr = sa[:i] + t + sa[i+j+1:]
            if not r or r > tr:
                r = tr

    if not r:
        return 'UNRESTORABLE'
    return r


print(main())


