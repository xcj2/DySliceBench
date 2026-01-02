MOD = 10**9 + 7
NUM_MAX = 10**5
is_prime = [True] * NUM_MAX
is_prime[0] = False
is_prime[1] = False
primes = []
for i in range(NUM_MAX):
    if is_prime[i]:
        primes.append(i)
        for j in range(2*i, NUM_MAX, i):
            is_prime[j] = False

def prime_fact(n):
    res = {}
    for p in primes:
        while n % p == 0:
            n //= p
            res[p] = res.get(p, 0) + 1
    if n > 1:
        res[n] = 1
    return res

def inv_pow(a, p):
    res = 1
    while p > 0:
        if p % 2 == 1:
            res = (res * a) % MOD
        p //= 2
        a = (a * a) % MOD
    return res

def comb(n, k):
    p, q = 1, 1
    for i in range(k):
        p = p * (n - i) % MOD
        q = q * (i + 1) % MOD
    return p * inv_pow(q, MOD-2) % MOD

def solve(n, m):
    v = prime_fact(m)
    ans = 1
    for k in v.values():
        ans = ans * comb(n+k-1, k) % MOD
    return ans % MOD

assert solve(2, 6) == 4
assert solve(3, 12) == 18
assert solve(100000, 1000000000) == 957870001

n, m = map(int, input().split())
print(solve(n, m))