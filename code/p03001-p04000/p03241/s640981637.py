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

# 速度調整版
def primes(n):
    sq = int(math.sqrt(n)+1)
    ss = 30030
    a = [None] * (ss)
    a[0] = 1
    t = 1
    for i in range(2,ss):
        if not a[i] is None:
            continue
        if t * i > ss:
            break
        t *= i
        for j in range(i*2,ss,i):
            a[j] = 1
    a = [i for i in range(t) if a[i] is None]
    d = collections.defaultdict(int)
    for i in a[1:]:
        while n % i == 0:
            n //= i
            d[i] += 1

    for j in range(1,sq//t+2):
        if j > n:
            break
        for ii in a:
            i = t*j+ii
            while n % i == 0:
                n //= i
                d[i] += 1
    if n > 1:
        d[n] += 1

    return d

# 約数をすべて返す
def divisions(n):
    d = primes(n)

    r = [1]
    for k, v in d.items():
        for c in r[:]:
            for i in range(1,v+1):
                r.append(c*(k**i))

    return sorted(r)


def main():
    n,m = LI()
    d = divisions(m)
    # print(len(d),d)
    r = 1
    for c in d:
        if c * n > m:
            break
        r = c

    return r


print(main())
