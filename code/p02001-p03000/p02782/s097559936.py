nmax = (10**6+1)*2
mod = 10**9+7

fac = [1]*nmax
finv = [1]*nmax
inv = [1]*nmax
def ncr_pre():
    for i in range(2,nmax):
        fac[i] = fac[i-1]*i % mod
        inv[i] = mod - inv[mod%i] * (mod//i) %mod
        finv[i] = finv[i-1] * inv[i] %mod

def ncr(n,r):
    if n<r:
        return 0
    if n<0 or r<0:
        return 0
    return fac[n]* (finv[r] * finv[n-r] %mod) %mod

def g(r,c):## r以下かつc以下の経路f(i,j)の総和
    ans = 0
    for i in range(1,r+2):
        ## f(i+1,c) =  f(i,0) + f(i,1) + ...f(i,c)
        ans += ncr(i+c,c)
        ans %=mod
    return ans

ncr_pre()
r1,c1,r2,c2 = map(int,input().split())
ans = g(r2,c2) - g(r1-1,c2) - g(r2,c1-1) + g(r1-1,c1-1)
print(ans % mod)
