#!python3

LI = lambda: list(map(int, input().split()))

# input
N, M = LI()

MOD = 10 ** 9 + 7
MAX = (10 ** 5) * 5 + 5
fac, finv, inv = [None] * MAX, [None] * MAX, [None] * MAX


def comb_init():
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1
    for i in range(2, MAX):
        fac[i] = fac[i - 1] * i % MOD
        inv[i] = -inv[MOD%i] * int(MOD / i) % MOD
        finv[i] = finv[i - 1] * inv[i] % MOD


def comb(n, k):
    if n < k or n < 0 or k < 0:
        return 0
    return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD


def perm(n, k):
    if n < k or n < 0 or k < 0:
        return 0
    return fac[n] * finv[n - k] % MOD


def main():
    comb_init()
    ans = 0
    v = perm(M, N)
    for i in range(N + 1):
        p = 1 if i % 2 == 0 else -1
        x = comb(N, i) * perm(M - i, N - i) % MOD
        ans = (ans + p * v * x) % MOD
    print(ans)
    

if __name__ == "__main__":
    main()
