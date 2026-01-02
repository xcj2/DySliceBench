#!python3

LI = lambda: list(map(int, input().split()))

# input
K = int(input())
S = input()

MOD = 10 ** 9 + 7
MAX = 2 * (10 ** 6) + 1
p25, p26 = [None] * MAX, [None] * MAX
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


def power_init():
    p25[0] = 1
    p26[0] = 1
    for i in range(1, MAX):
        p25[i] = p25[i - 1] * 25 % MOD
        p26[i] = p26[i - 1] * 26 % MOD


def main():
    comb_init()
    power_init()
    n = len(S)
    ans = 0
    for i in range(K + 1):
        x = p25[i] * comb(i + n - 1, n - 1) % MOD * p26[K - i] % MOD
        ans = (ans + x) % MOD
    print(ans)


if __name__ == "__main__":
    main()
