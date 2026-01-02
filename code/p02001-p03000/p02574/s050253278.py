import bisect
import sys,io
import math
from collections import deque
from heapq import heappush, heappop
import functools
input = sys.stdin.buffer.readline

def sRaw():
    return input().decode("utf-8").rstrip("\n").rstrip("\r")


def iRaw():
    return int(input())

def ssRaw():
    return input().split()


def isRaw():
    return list(map(int, ssRaw()))

INF = 1 << 29

DIV = (10**9) + 7
#DIV = 998244353

def mod_inv_prime(a, mod=DIV):
    return pow(a, mod-2, mod)


def mod_inv(a, b):
    r = a
    w = b
    u = 1
    v = 0
    while w != 0:
        t = r//w
        r -= t*w
        r, w = w, r
        u -= t*v
        u, v = v, u
    return (u % b+b) % b


def CONV_TBL(max, mod=DIV):
    fac, finv, inv = [0]*max, [0]*max, [0]*max
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1
    for i in range(2, max):
        fac[i] = fac[i-1]*i % mod
        inv[i] = mod - inv[mod % i] * (mod//i) % mod
        finv[i] = finv[i-1]*inv[i] % mod

    class CONV:
        def __init__(self):
            self.fac = fac
            self.finv = finv
            pass

        def ncr(self, n, k):
            if(n < k):
                return 0
            if(n < 0 or k < 0):
                return 0
            return fac[n]*(finv[k]*finv[n-k] % DIV) % DIV

    return CONV()


def cumsum(As):
    s = 0
    for a in As:
        s += a
        yield s


sys.setrecursionlimit(200005)


def dijkstra(G,start=0):
    heap = []
    cost = [INF]*len(G)
    heappush(heap,(0,start))
    while len(heap)!=0:
        c,n = heappop(heap)
        if cost[n] !=INF:
            continue
        cost[n]=c
        for e in G[n]:
            ec,v = e
            if cost[v]!=INF:
                continue
            heappush(heap,(ec+c,v))
    return cost

def gcd_list(As):
    return functools.reduce(math.gcd, As)

def lcm_div(x, y):
    return ((x * y) // math.gcd(x, y))%DIV

def lcm_div_list(numbers):
    return functools.reduce(lcm_div, numbers, 1)%DIV

def primes_by_eratos(n):
    data = [i for i in range(2, n + 1)]
    for d in data:
        data = [x for x in data if (x == d or x % d != 0)]
    return data

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

def main():
    N = iRaw()
    As = isRaw()
    gcds = gcd_list(As)
    if gcds!=1:
        print("not coprime")
        return
    lcms = lcm_div_list(As)
    mul_d = 1
    lcm_d = 1
    primes = primes_by_eratos(1000)
    lcm_yakus = {}

    for a in As:
        yakus = set(prime_factorize(a))
        for y in yakus:
            if y in lcm_yakus:
                print('setwise coprime')
                return
            else:
                lcm_yakus[y]=1
    print("pairwise coprime")
    return
    
main()
