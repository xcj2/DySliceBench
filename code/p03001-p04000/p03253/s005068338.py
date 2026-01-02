from itertools import groupby

N, M = map(int, input().split())
mod = 10 ** 9 + 7


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


def make_table(n, mod=10 ** 9 + 7):
    N = n
    # 元テーブル
    g1 = [0] * (N + 1)
    g1[0] = 1
    g1[1] = 1

    # 逆元テーブル
    g2 = [0] * (N + 1)
    g2[0] = 1
    g2[1] = 1

    # 逆元テーブル計算用テーブル
    inverse = [0] * (N + 1)
    inverse[0] = 0
    inverse[1] = 1

    for i in range(2, N + 1):
        g1[i] = (g1[i - 1] * i) % mod
        inverse[i] = (-inverse[mod % i] * (mod // i)) % mod
        g2[i] = (g2[i - 1] * inverse[i]) % mod

    return g1, g2


def main():
    def cmb(n, r, mod):
        if r < 0 or r > n:
            return 0
        r = min(r, n - r)
        return g1[n] * g2[r] * g2[n - r] % mod

    p = [len(list(j)) for i, j in groupby(prime_factorize(M))]
    g1, g2 = make_table(10 ** 6, mod)
    answer = 1
    for i in p:
        answer *= cmb(i + N - 1, N - 1, mod)
        answer %= mod

    print(answer)


if __name__ == '__main__':
    main()
