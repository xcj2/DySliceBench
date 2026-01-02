from sys import stdin

MAX = 10 ** 6
MOD = 10 ** 9 + 7
fac = [0] * MAX
finv = fac[:]
inv = fac[:]


def cmb_init():
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1
    for i in range(2, MAX):
        fac[i] = fac[i - 1] * i % MOD
        inv[i] = MOD - inv[MOD % i] * (MOD // i) % MOD
        finv[i] = finv[i - 1] * inv[i] % MOD


def cmb(n, k):
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD


def main():
    X, Y = [int(x) for x in stdin.readline().rstrip().split()]
    if (X + Y) % 3:
        print(0)
    else:
        m = (2 * X - Y) // 3
        n = X - 2 * m
        if n < 0 or m < 0:
            print(0)
        else:
            cmb_init()
            ans = cmb(n + m, min(n, m))
            print(ans)


if __name__ == "__main__":
    main()
