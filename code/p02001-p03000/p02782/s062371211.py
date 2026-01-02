r1, c1, r2, c2 = map(int, input().split())

mod = 1000000007

def pow(x, n):
    ret = 1
    while n > 0:
        if (n & 1) == 1:
            ret = (ret * x) % mod
        x = (x * x) % mod
        n //= 2
    return ret

def fac(n):
    ret = 1
    for i in range(1, n + 1):
        ret = (ret * i) % mod
    return ret

def facinv(n):
    return pow(fac(n), mod - 2)

def cmb(n, k):
    if k < 0 or k > n:
        return 0
    return ((fac(n) * facinv(k)) % mod * facinv(n - k)) % mod

def rect(r, c):
    return cmb(r + c, c)

ret = (rect(r2 + 1, c2 + 1) - rect(r1, c2 + 1) - rect(r2 + 1, c1) + rect(r1, c1) + mod + mod) % mod
print(ret)
