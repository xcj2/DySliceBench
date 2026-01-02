import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools
from collections import deque

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

DR = [1, -1, 0, 0]
DC = [0, 0, 1, -1]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()

fac = [-1] * (10**6+1)
inv = [-1] * (10**6+1)
finv = [-1] * (10**6+1)

fac[0] = fac[1] = 1
inv[1] = 1
finv[0] = finv[1] = 1

def initNCMMod(limit):
    for i in range(2, limit):
        inv[i] = mod - inv[mod%i] * (mod // i) % mod

initNCMMod(10**6+1)

def integer_factorization(n):
    prime_count = collections.Counter()
    for i in range(2, int(math.sqrt(n)) + 2):
        while n % i == 0:
            n //= i
            prime_count[i] += 1
    if n > 1:
        prime_count[n] += 1
    return prime_count

def modpow(x, n):
    ans = 1
    while(n > 0):
        if(bin(n & 1) == bin(1)):
            ans = ans*x % mod
        x = x*x % mod
        n = n >> 1
    return ans % mod

def main():
    N = I()
    A = LI()
    kobaisu = collections.defaultdict(int)
    div = [1] * N
    for i, a in enumerate(A):
        d = integer_factorization(a)
        for k, v in d.items():
            kobaisu[k] = max(kobaisu[k], v)
            div[i] *= modpow(k, v)
            div[i] %= mod

    kobai = 1
    for k, v in kobaisu.items():
        kobai *= modpow(k, v)
        kobai %= mod

    ans = 0
    for d in div:
        ans += kobai * inv[d] % mod
        ans %= mod
    print(ans)
main()

