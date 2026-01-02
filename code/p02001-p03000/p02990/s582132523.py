#template
def inputlist(): return [int(k) for k in input().split()]
#template
N,K = inputlist()
mod = 10**9+7
def pow_k(a,n,mod):
    if n == 0:
        return 1
    if n % 2 ==0:
        return pow_k(a*a % mod,n//2,mod)
    else:
        return a * pow_k(a,n-1,mod) % mod
def modinv(a, mod):
    return pow(a, mod-2, mod)
def combination(n, r, mod=10**9+7):
    r = min(r, n-r)
    res = 1
    for i in range(r):
        res = res * (n - i) * modinv(i+1, mod) % mod
    return res
for i in range(1,K+1):
    if i <= N-K+1:
        ans = combination(N-K+1,i,mod) * combination(K-1,i-1,mod)
        ans %= mod
        print(ans)
        continue
    print(0)