from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,copy,time
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 998244353
eps = 10**-7
def inp(): return int(input())
def inpl(): return list(map(int, input().split()))
def inpl_str(): return list(input().split())


# 先にふるってprimesを作る
def hurui(N):
    koho = list(range(2,N))
    prime = []
    limit = math.sqrt(koho[-1])
    while True:
        p = koho[0]
        if limit <= p:
            prime = prime + koho
            break
        else:
            prime.append(p)
            koho = [e for e in koho if e%p != 0]

    return prime

# N を素因数分解
def factorization(N):
    ans = defaultdict(int)
    L = len(primes)
    pind = 0
    while N > 1:
        p = primes[pind]
        while N%p == 0:
            N //= p
            ans[p] += 1
        pind += 1
        if pind >= L:
            ans[N] += 1
            break
    return ans

N,P = inpl()

primes = hurui(int(math.sqrt(P))+3)
facs = factorization(P)

ans = 1
for p,n in facs.items():
    if n >= N:
        ans *= p**(n//N)

print(ans)
