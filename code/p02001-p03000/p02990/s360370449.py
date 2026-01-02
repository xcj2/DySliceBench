import sys
readline = sys.stdin.buffer.readline
n,k = map(int,readline().split())
r = n-k
mod = 10**9+7
def pow(n,p,mod=10**9+7): #繰り返し二乗法(nのp乗)
    res = 1
    while p > 0:
        if p % 2 == 0:
            n = n ** 2 % mod
            p //= 2
        else:
            res = res * n % mod
            p -= 1
    return res % mod
def factrial_memo(n=10**5+1,mod=10**9+7):
    fact = [1, 1]
    for i in range(2, n + 1):
        fact.append((fact[-1] * i) % mod)
    return fact
def fermat_cmb(n, r, mod=10**9+7): #needs pow,factrial_memo(only fact). return nCk
    return fact[n] * pow(fact[r],mod-2) * pow(fact[n-r],mod-2) %mod
fact = factrial_memo()
for i in range(1,k+1):
    if r+1 < i:
        print(0)
        continue

    res = fermat_cmb(r+1,i)*fermat_cmb(k-1,k-i)
    print(res%mod)
    
