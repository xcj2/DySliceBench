MAX = 510000
MOD = 1000000007

fac = [0] * MAX
finv = [0] * MAX
inv = [0] * MAX

def comb_init():
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1
    for i in range(2, MAX):
        fac[i] = fac[i - 1] * i % MOD
        inv[i] = MOD - inv[MOD % i] * (MOD // i) % MOD
        finv[i] = finv[i - 1] * inv[i] % MOD
        
def comb(n, r):
    if n < r:           return 0
    if n < 0 or r < 0:  return 0
    return fac[n] * (finv[r] * finv[n - r] % MOD) % MOD

def solve():
    ans = 0
    an = H + B - A - 1
    ar = B
    bn = W + A - B - 2
    br = W - B - 1
    for i in range(W-B):
        a = comb(an, ar)
        b = comb(bn, br)
        ans += (a * b) % MOD
        an += 1; ar += 1
        bn -= 1; br -= 1
    return ans % MOD

H, W, A, B = map(int, input().split())

comb_init()
print(solve())
