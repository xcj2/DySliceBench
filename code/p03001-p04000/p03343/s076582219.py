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
    n,k,q = LI()
    a = LI() + [-1]
    sa = sorted(a)
    r = sa[-1] - sa[0]
    # print(sorted([[a[i],i] for i in range(n)]))
    for i in range(1,n+1):
        if sa[i] == sa[i-1]:
            continue
        mi = sa[i]
        b = []
        c = 0
        for j in range(n+1):
            if a[j] < mi:
                if j - c >= k:
                    b += sorted(a[c:j])[:j-c-k+1]
                c = j + 1
        if len(b) < q:
            continue
        b.sort()
        t = b[q-1] - mi
        if r > t:
            r = t


    return r




print(main())

