import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
n,m,k = map(int,readline().split())
mod = 998244353
 
if m == 1:
    if k < n-1:
        print(0)
    else:
        print(1)
    exit()

def pow(n,p,mod=mod): #繰り返し二乗法(nのp乗)
    res = 1
    while p > 0:
        if p % 2 == 0:
            n = n ** 2 % mod
            p //= 2
        else:
            res = res * n % mod
            p -= 1
    return res % mod

def factrial_memo(n=2*10**5,mod=mod):
    fact = [1, 1]
    for i in range(2, n + 1):
        fact.append((fact[-1] * i) % mod)
    return fact
fact = factrial_memo()

def fermat_cmb(n, r, mod=mod): #needs pow,factrial_memo(only fact). return nCk
    return fact[n] * pow(fact[r],mod-2) * pow(fact[n-r],mod-2) %mod
ans = 0
for i in range(k+1):
    res = m*pow(m-1,n-1-i) #塊を含めて分けられるもの達
    ans += res*fermat_cmb(n-1,i)%mod
print(ans%mod)