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
    s = S()
    t = S()
    l = len(s)
    d = collections.defaultdict(lambda: None)
    e = collections.defaultdict(lambda: None)
    for i in range(l):
        si = s[i]
        ti = t[i]
        if not d[si] is None:
            if ti != d[si]:
                return 'No'
        if not e[ti] is None:
            if si != e[ti]:
                return 'No'
        d[si] = ti
        e[ti] = si

    return 'Yes'


print(main())
