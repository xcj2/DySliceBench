import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
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
    n = I()
    d = collections.defaultdict(int)
    d[''] = 1
    t = [
            'AGC',
            'ACG',
            'GAC',
            'AGAC',
            'AGCC',
            'AGTC',
            'ACGC',
            'AGGC',
            'ATGC'
        ]
    for i in range(n):
        e = collections.defaultdict(int)
        for c,v in d.items():
            v %= mod
            for g in 'ACGT':
                if c + g in t or (c + g)[-3:] in t:
                    continue
                e[(c + g)[-3:]] += v
        d = e

    return sum(d.values()) % mod


print(main())


