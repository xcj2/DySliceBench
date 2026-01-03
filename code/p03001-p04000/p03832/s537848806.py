import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**5) 
 
def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

def fact(n: int, mod: int):
    fac = []
    for i in range(n+1):
        fac.append(1 if i < 2 else i * fac[-1] % mod)
        
    return fac

def fact_inv(fac: list, mod: int):
    return [1 if i < 2 else pow(faci, mod-2, mod) for i, faci in enumerate(fac)]

def nCr(n: int, r: int, mod: int, fac: list, fac_inv: list):
    return fac[n] * fac_inv[r] * fac_inv[n-r] % mod

def nPr(n: int, r: int, mod: int, fac: list, fac_inv: list):
    return fac[n] * fac_inv[n-r] % mod



n,a,b,c,d = li()
MOD = 10**9+7

dp = [[0]*(n+1) for _ in range(n+1)]
dp[0][0] = 1


fac = fact(n, MOD)
fac_inv = fact_inv(fac, MOD)

fac_i_k_mod = [[0]*(n+1) for _ in range(n+1)]
fac_inv_i_k_mod = [[0]*(n+1) for _ in range(n+1)]
for i in range(n+1):
    for k in range(n+1):
        fac_i_k_mod[i][k] = pow(fac[i], k, MOD)
        
for i in range(n+1):
    for k in range(n+1):
        fac_inv_i_k_mod[i][k] = pow(fac_i_k_mod[i][k], MOD-2, MOD)        


for i in range(1, n+1):
    for j in range(n+1):
        dp[i][j] += dp[i-1][j]
        if i < a or i > b:
            continue
        
        for k in range(c, min(d, j//i)+1):
            if j-i*k < 0:
                continue
            
            dp[i][j] += dp[i-1][j-i*k] * nPr(j, i*k, MOD, fac, fac_inv) % MOD\
                        * fac_inv_i_k_mod[i][k] % MOD\
                        * fac_inv[k] % MOD
            dp[i][j] %= MOD
            
print(dp[n][n])
