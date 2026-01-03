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

# nの階乗のリスト
def fact(n:int, mod:int) -> list:
    fac = [1,1]
    res = 1
    for i in range(2,n+1):
        res = res*i%mod
        fac.append(res)
    return fac

n,m = li()
MOD = 10**9 + 7

if m > n:
    n, m = m, n
    
fac = fact(n,MOD)

if n-m > 1:
    print(0)

elif n-m == 1:
    print((fac[n] * fac[m]) % MOD)
    
else:
    print((2 * fac[n] * fac[m]) % MOD)
        
    