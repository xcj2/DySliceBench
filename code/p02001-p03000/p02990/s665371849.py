from sys import stdin, setrecursionlimit


def initialize_cmb(m, mod=10 ** 9 + 7):
    fac = [1]
    finv = [1]
    inv = [0] * (m + 1)
    if m >= 1:
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
    mod = 10 ** 9 + 7
    input = stdin.buffer.readline
    n, k = map(int, input().split())

    fac, finv = initialize_cmb(n, mod)

    for i in range(1, k + 1):
        print(cmb(n - k + 1, i, fac, finv, mod) * cmb(k - 1, i - 1, fac, finv, mod) % mod)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
