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
    a = [2**(ord(c)-97) for c in S()]
    b = [0]
    d2 = {}
    d2[0] = 0
    c = 0
    ii = [2**i for i in range(26)]
    for t,i in zip(a, range(1,len(a)+1)):
        c ^= t
        tr = inf
        if c in d2:
            tr = d2[c] + 1

        for j in ii:
            e = c ^ j
            if e in d2 and d2[e] + 1 < tr:
                tr = d2[e] + 1
        if c not in d2 or d2[c] > tr:
            d2[c] = tr
    return d2[c] if d2[c] else 1



print(main())


