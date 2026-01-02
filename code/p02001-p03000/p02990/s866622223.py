N, K = map(int, input().split())
R = N - K
mod = 10 ** 9 + 7


def makeTableMod(N, mod=10 ** 9 + 7):
    fac = [1 for i in range(N)]
    finv = [1 for i in range(N)]
    inv = [1 for i in range(N)]
    for i in range(2, N):
        fac[i] = fac[i - 1] * i % mod
        inv[i] = mod - inv[mod % i] * (mod // i) % mod
        finv[i] = finv[i - 1] * inv[i] % mod
    return fac, finv


fac, finv = makeTableMod(2001, mod)


def binomialCoefficient(N, r, mod=10 ** 9 + 7):
    if N < r:
        return 0
    else:
        return fac[N] * (finv[r] * finv[N - r] % mod) % mod


def solve(i):
    # (N-K+1, i) * (K-1, i-1)を計算すれば良い
    ans = binomialCoefficient(N-K+1, i) * binomialCoefficient(K-1, i-1) % mod
    return ans


for i in range(K):
    if i == 0:
        print((R+1) % mod)
    else:
        ans = solve(i+1)
        print(ans % mod)