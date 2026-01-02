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

def main():
    n = I()
    d = collections.defaultdict(int)
    pr = Prime(10000)
    r = 0

    for i in range(2,n+1):
        t = pr.division(i)
        for k,v in t:
            d[k] += v
    c = collections.defaultdict(int)
    for k,v in d.items():
        if v >= 74:
            c[75] += 1
        if v >= 24:
          c[25] += 1
        if v >= 14:
          c[15] += 1
        if v >= 4:
          c[5] += 1
        if v >= 2:
            c[3] += 1

    r += c[75]
    r += c[25] * (c[3]-1)
    r += c[15] * (c[5]-1)
    if c[5] > 1:
        r += c[5] * (c[5]-1) // 2 * (c[3]-2)


    return r


print(main())
