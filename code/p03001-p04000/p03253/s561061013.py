import sys
stdin = sys.stdin

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

from collections import Counter

# nの逆元のリスト
def inv_mod(n:int, mod:int) -> list:
    inv = [0,1]
    for i in range(2,n+1):
        inv.append(mod - ((mod//i)*inv[mod%i]) % mod)
    return inv
       
# nの階乗のリスト
def fact(n:int, mod:int) -> list:
    fac = [1,1]
    res = 1
    for i in range(2,n+1):
        res = res*i%mod
        fac.append(res)
    return fac

# nの階乗の逆元のリスト
def fact_inv(n:int, inv:list, mod:int) -> list:
    facInv = [1,1]
    for i in range(2,n+1):
        facInv.append(facInv[i-1]*inv[i] % mod)
    return facInv
        
# 二項係数
def nCr(n:int, r:int, mod:int, fac:list, facInv:list) -> int:
    if not (0<=r and r<=n):
        return 0
    
    return ((fac[n]*facInv[r]) % mod) * facInv[n-r] % mod

def factorize(n: int):
    d = Counter()
    m= 2
    
    while m*m <= n:
        while n%m == 0:
            n //= m
            d[m] += 1
            
        m += 1
        
    if n > 1:
        d[n] += 1
        
    return d


n,m = li()

MOD = 10**9+7

# 二項係数の準備
inv = inv_mod(n+100,MOD)
fac = fact(n+100,MOD)
facInv = fact_inv(n+100,inv,MOD)


primes = factorize(m)
ans = 1

if n == 1 or m == 1:
    print(ans)
else:
    for pi in primes.values():
        ans = ans * nCr(n+pi-1, pi, MOD, fac, facInv) % MOD
    print(ans)
