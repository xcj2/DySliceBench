import math

def xgcd(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

def modinv(a, m):
    g, x, y = xgcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def combination(n,r,mod):
    r = min(r,n-r)

    res = 1
    for i in range(r):
        res = res * (n-i) * modinv(i+1,mod) % mod
    
    return res

mod = 10**9+7

n,a,b = map(int,input().split())

ans = pow(2,n,mod) - 1

ans -= combination(n,a,mod)
ans -= combination(n,b,mod)

print(ans % mod)
