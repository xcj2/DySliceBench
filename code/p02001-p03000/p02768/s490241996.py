def pow_mod(n, k, m):
    r = 1
    while k:
        if k & 1:
            r = (r * n) % m
        n = (n * n) % m
        k >>= 1
    return r

def comb(n, r):
    numerator, denominator = 1, 1
    for i in range(n - (r - 1), n + 1):
        numerator = (numerator * i) % (10**9 + 7)
    for i in range(1, r + 1):
        denominator = (denominator * i) % (10**9 + 7)
    inv = pow(denominator, 10**9 + 7 - 2, 10**9 + 7)
    return (numerator * inv) % (10**9 + 7)

def mod_minus(a, b, m):
    if a < b:
        return a + m - b
    else:
        return a - b

n, a, b = map(int, input().split())
count = pow_mod(2, n, 10**9 + 7) - 1
count = mod_minus(count, comb(n, a), 10**9 + 7)
count = mod_minus(count, comb(n, b), 10**9 + 7)
print(count)