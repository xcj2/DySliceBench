MOD = int(1e9+7)

def fast_power(b, e):
    res = 1
    while e > 0:
        if e % 2 == 1:
            res = res * b % MOD
        b = b * b % MOD
        e >>= 1
    return res

def mod_inverse(n):
    return fast_power(n, MOD-2)
def mul(x, y):
    return ((x % MOD) * (y % MOD) % MOD + MOD) % MOD
def multiply(x, y, z):
    return mul(mul(x, y), z)

def nCr(n, r):
    if r == 0:
        return 1
    fac = [1] * (n+1)
    for i in range(1, n+1):
        fac[i] = fac[i-1] * i % MOD
    # n! / (r! * (n-r)!)
    return multiply(fac[n], mod_inverse(fac[r]), mod_inverse(fac[n-r]))

x, y = map(int, input().split())
n = (2*x-y) // 3
m = (2*y-x) // 3
if min(n, m) < 0 or (x+y)%3 != 0:
    print(0)
    exit()
print(nCr(m+n, n))
