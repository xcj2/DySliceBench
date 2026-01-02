r1, c1, r2, c2 = map(int, input().split())
mod = 10 ** 9 + 7

# dp = [[0] * (r2 + 1) for _ in range(c2 + 1)]
# for i in range(c2 + 1):
#     dp[i][0] = 1
# for i in range(r2 + 1):
#     dp[0][i] = 1

# for i in range(c2):
#     for j in range(r2):
#         dp[i + 1][j + 1] = dp[i + 1][j] + dp[i][j + 1]

# ans = 0
# for i in range(c1, c2 + 1):
#     for j in range(r1, r2 + 1):
#         ans += dp[i][j]
# print(ans % mod)
# brute forceであり、TLEする。


MAX = 10 ** 6 * 2 + 5
def com_init(MAX, mod):
    fac = [0] * MAX
    finv = [0] * MAX
    inv = [0] * MAX
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1
    for i in range(2, MAX):
        fac[i] = fac[i - 1] * i % mod
        inv[i] = mod - inv[mod % i] * (mod // i) % mod
        finv[i] = finv[i - 1] * inv[i] % mod
    return fac, finv

fac, finv = com_init(MAX, mod)

def nCr(n,r):
    return fac[n] * (finv[r] * finv[n - r] % mod) % mod 

def myfunc(r, c):
    return nCr(r + c + 2, r + 1) - 1


ans = myfunc(r2, c2)
ans -= myfunc(r2, c1 - 1)
ans -= myfunc(r1 - 1, c2)
ans += myfunc(r1 - 1, c1 - 1)
print(ans % mod)

# The result is the same as the below, but much faster.
# def nCr(n, r):
#     return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
