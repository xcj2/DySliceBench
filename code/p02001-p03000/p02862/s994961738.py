import math
X, Y = map(int, input().split())
p = (((X+Y)/3)+Y-X)/2
m = p+X-Y


def framod(n, mod, a=1):
    for i in range(1,n+1):
        a=a * i % mod
    return a

def power(n, r, mod):
    if r == 0: return 1
    if r%2 == 0:
        return power(n*n % mod, r//2, mod) % mod
    if r%2 == 1:
        return n * power(n, r-1, mod) % mod

def comb(n, k, mod):
    a=framod(n, mod)
    b=framod(k, mod)
    c=framod(n-k, mod)
    return (a * power(b, mod-2, mod) * power(c, mod-2, mod)) % mod


if p % 1 != 0 or p<0 or m<0:
    ans = 0

else:
    q = p+m
    q = int(q)
    p = int(p)
    ans = comb(q,p,10**9+7)
  

print(ans)