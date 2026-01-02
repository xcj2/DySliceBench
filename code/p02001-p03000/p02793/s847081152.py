from collections import Counter

def extended_euclid(a, b):
    x1, y1, m = 1, 0, a
    x2, y2, n = 0, 1, b
    while m % n != 0:
        q, r = divmod(m, n)
        x1, y1, m, x2, y2, n = x2, y2, n, x1 - q * x2, y1 - q * y2, r
    return (x2, y2, n)

def modular_inverse(a, mod):
    x, _, g = extended_euclid(a, mod)
    if g != 1:
        return None # Modular inverse of a does not exist
    else:
        return x % mod

def prime_factorization(n):
    '''
    Trial division.
    Input: 
        n : a positive integer
    Output:
        a dictionary of #(each prime factors) of n,
    '''
    result = []
    app = result.append
    if n < 2:
        return Counter()
    while n % 2 == 0:
        app(2)
        n //= 2
    p = 3
    while p*p <= n:
        while n % p == 0:
            app(p)
            n //= p
        p += 2
    if n > 1:
        app(n)
    return Counter(result)

MOD = 10**9 + 7

N = int(input())
*A, = map(int, input().split())
ans = 0
lcm = {}
for a in A:
    for x, y in prime_factorization(a).items():
        if x not in lcm.keys():
            lcm[x] = y
        else:
            lcm[x] = max(lcm[x], y)
L = 1
for x, y in lcm.items():
    L *= pow(x, y, MOD)
    L %= MOD
for a in A:
    ans += L * modular_inverse(a, MOD)
    ans %= MOD
print(ans)