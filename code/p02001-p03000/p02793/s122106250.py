def gcd(x, y):
    while y > 0:
        r = x%y
        x = y
        y = r
    return x

def lcm(x, y):
    return x//gcd(x, y)*y

def modpow(x, n, mod):
    res = 1
    while n > 0:
        if n%2 == 1:
            res = res*x%mod
        x = x*x%mod
        n >>= 1
    return res

mod = 10**9+7

n = int(input())
a = list(map(int, input().split()))

g = 0
for x in a:
    g = gcd(g, x)

l = 1
for i in range(n):
    a[i] //= g
    l = lcm(l, a[i])
l %= mod

ans = 0
for i in range(n):
    ans += l*modpow(a[i], mod-2, mod)
    ans %= mod

print(ans)