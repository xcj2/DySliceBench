def factorize(n):
    b = 2
    fct = [(1,1)]
    while b * b <= n:
        cnt =0
        while n % b == 0:
            n //= b
            cnt +=1
        if cnt >=1:
            fct.append((b,cnt))
        b = b + 1
    if n > 1:
        fct.append((n,1))
    return fct

nmax = 10**6
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

ncr_pre()
n,m = map(int,input().split())
ls = factorize(m)
tmp = 1
for num,cnt in ls:
    if num==1:continue

    tmp=tmp*ncr(n+cnt-1,cnt) %mod
print(tmp)
