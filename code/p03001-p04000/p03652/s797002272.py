import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()

def gcd(a,b):
    while b>0:
        a,b = b,a
        b %= a
    return a

def main():
    n,m = LI()
    a = [LI() for _ in range(n)]
    ai = [0] * n
    d = collections.defaultdict(int)
    for i in range(n):
        d[a[i][0]] += 1
    dr = r = max(d.values())
    s = set(list(range(1,m+1)))
    while s:
        for k,v in d.items():
            if v == dr:
                s.remove(k)
        if not s:
            break
        d = collections.defaultdict(int)
        for i in range(n):
            while a[i][ai[i]] not in s:
                ai[i] += 1
        for i in range(n):
            d[a[i][ai[i]]] += 1
        dr = max(d.values())
        if r > dr:
            r = dr
    return r


print(main())



