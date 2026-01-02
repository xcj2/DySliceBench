import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,copy,functools
import random

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return list(map(int, sys.stdin.readline().split()))
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)

class Prime():
    def __init__(self, n):
        self.M = m = int(math.sqrt(n)) + 10
        self.A = a = [True] * m
        a[0] = a[1] = False
        self.T = t = []
        for i in range(2, int(math.sqrt(m)) + 1):
            if not a[i]:
                continue
            t.append(i)
            for j in range(i*i,m,i):
                a[j] = False

    def is_prime(self, n):
        return self.A[n]

    def division(self, n):
        d = collections.defaultdict(int)
        for c in self.T:
            while n % c == 0:
                d[c] += 1
                n //= c
            if n < 2:
                break
        if n > 1:
            d[n] += 1
        return d.items()

    def sowa(self, n):
        r = 1
        for k,v in self.division(n):
            t = 1
            for i in range(1,v+1):
                t += math.pow(k, i)
            r *= t
        return r


def main():
    n = I()
    ac = collections.Counter(LI())
    if n == 2:
        return max(ac.keys())
    a = []
    aa = []
    for k,v in ac.items():
        if v > 1:
            aa.append(k)
        else:
            a.append(k)

    tr = -1
    if len(aa) > 0:
        tr = aa[0]
        for k in aa[1:]:
            tr = fractions.gcd(k,tr)

    l = len(a)
    if l < 2:
        return tr
    if l < 3:
        r = 1
        for i in a:
            kr = fractions.gcd(i,tr)
            if r < kr:
                r = kr
        return r

    m = max(a)
    lm = m // (l-1)
    pr = Prime(10**9)
    p = collections.defaultdict(int)

    for b in a:
        r = [1]
        for k, v in pr.division(b):
            for c in r[:]:
                for i in range(1,v+1):
                    t = c*(k**i)
                    if t > lm:
                        break
                    r.append(t)
        for k in r:
            p[k] += 1



    if tr == -1:
        r = 1
        for k,v in p.items():
            if v >= l-1 and r < k:
                r = k
        return r

    r = 1
    for k,v in p.items():
        kk = fractions.gcd(tr,k)
        if v >= l-1 and r < kk:
            r = kk

    return r


print(main())

