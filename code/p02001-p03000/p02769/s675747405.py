from sys import stdin, setrecursionlimit


def initialize_cmb(m, mod=10 ** 9 + 7):
    fac = [1]
    finv = [1]
    inv = [0] * (m + 1)
    if m > 1:
        fac.append(1)
        finv.append(1)
        inv[1] = 1
        pre_fac = 1
        pre_finv = 1
        for i in range(2, m + 1):
            pre_fac = pre_fac * i % mod
            fac.append(pre_fac)
            inv[i] = mod - inv[mod % i] * (mod // i) % mod
            pre_finv = pre_finv * inv[i] % mod
            finv.append(pre_finv)
    return fac, finv


def cmb(n, k, fac, finv, mod=10 ** 9 + 7):
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fac[n] * (finv[k] * finv[n - k] % mod) % mod


def main():
    input = stdin.buffer.readline
    mod = 10 ** 9 + 7
    n, k = map(int, input().split())

    fac, finv = initialize_cmb(n, mod)

    c_n = []
    for i in range(n + 1):
        c_n.append(cmb(n, i, fac, finv))
    c_n_1 = []
    for i in range(n):
        c_n_1.append(cmb(n - 1, i, fac, finv))

    ans = 0
    for i in range(min(k + 1, n)):
        ans += c_n[i] * c_n_1[n - i - 1]
        ans %= mod
    print(ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
