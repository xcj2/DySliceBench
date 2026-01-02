def modpow(a,n,p):
    l = len(bin(n))-2
    res = 1
    for i in range(l):
        if n>>i &1:
            res = (res*a) % p
        a = (a**2) % p
    return res

def ncr_1(n,r,p):##　n>>r の場合のncr　O(r)
    x = 1
    y = 1
    for i in range(r):
        x*=(n-i)
        y*=(i+1)
        x%=p
        y%=p
    return x*modinv(y,p) %mod

def modinv(a,p):
    b,u,v = p,1,0
    while b:
        t = a//b
        a -= t*b
        a,b = b,a
        u -=t*v
        u,v = v,u
    u %=p
    return u


nmax = 10**6
mod = 10**9+7

n,a,b = map(int,input().split())
ans = modpow(2,n,mod) - 1 - ncr_1(n,a,mod) - ncr_1(n,b,mod)
print(ans%mod)
