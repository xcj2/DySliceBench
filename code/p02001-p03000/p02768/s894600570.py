def e(x, y):
    c0, c1 = x, y
    a0, a1 = 1, 0
    b0, b1 = 0, 1

    while c1 != 0:
        m = c0 % c1
        q = c0 // c1

        c0, c1 = c1, m
        a0, a1 = a1, (a0 - q * a1)
        b0, b1 = b1, (b0 - q * b1)

    return c0, a0, b0

def c(n,r):
    ngo = 1
    ngoo = 1
    for i in range(min(n,r)):
        ngo*=(n-i)
        ngoo*=(i+1)
        ngoo%=(10**9+7)
        ngo%=(10**9+7)
        #ngo %= (10**9+7)
        #ngoo %= (10**9+7)
    return (ngo*e(ngoo,10**9+7)[1])%(10**9+7)
    
def beki(x,y):
    if y == 0:
        return 1
    if y == 1:
        return x
    if y %2 == 0:
        return beki((x**2)%(10**9+7),y//2)%(10**9+7)
    else:
        return x*beki(x,y-1)%(10**9+7)
    
import math
n,a,b = map(int,input().split())
ngo = (beki(2,n)-1)%(10**9+7)
ans = (ngo-c(n,a)-c(n,b))
print(ans%(10**9+7))