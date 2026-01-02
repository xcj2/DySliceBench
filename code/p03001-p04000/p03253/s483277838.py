import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(): return [list(map(int, l.split())) for l in sys.stdin.readlines()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)
def pe(s): return print(str(s), file=sys.stderr)
def JA(a, sep): return sep.join(map(str, a))
def JAA(a, s, t): return s.join(t.join(map(str, b)) for b in a)

def divisions(n):
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
        if t*j > n:
            break
        for ii in a:
            i = t*j+ii
            while n % i == 0:
                n //= i
                d[i] += 1

    if n > 1:
        d[n] += 1

    return d

def inv(x):
    return pow(x, mod - 2, mod)

cms = 10**5 + 100
cm = [0] * cms

def comb_init():
    cm[0] = 1
    for i in range(1, cms):
        cm[i] = cm[i-1] * i % mod

def comb(a, b):
    return (cm[a] * inv(cm[a-b]) % mod) * inv(cm[b]) % mod

def main():
    n,m = LI()

    comb_init()
    d = divisions(m)
    r = 1
    for v in d.values():
        r *= comb(n+v-1,v)
        r %= mod

    return r


print(main())

