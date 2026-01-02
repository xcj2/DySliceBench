def mod_inv(value):
    b = mod
    u = 1
    v = 0
    while b:
        t = value // b
        value -= t * b
        b, value = value, b
        u -= t * v
        v, u = u, v
    u %= mod
    if u < 0:
        u += mod
    return u

def calcFact():
    fact[0] = 1
    fact_inv[0] = 1
    for i in range(1, 2010):
        fact[i] = i * fact[i - 1]
        fact[i] %= mod
        fact_inv[i] = mod_inv(fact[i])
    return

def comb(n, r):
    if r == 0:
        return 1
    return fact[n] * fact_inv[r] % mod * fact_inv[n - r] % mod

fact = [0 for i in range(2020)]
fact_inv = [0 for i in range(2020)]

mod = 1000000007

N, K = map(int, input().split())
calcFact()

for i in range(1, K + 1):
    if N - K + 1 < i:
        print(0)
        continue
    ans = comb(K - 1, i - 1) * comb(N - K + 1, i) % mod
    print(ans)
    
