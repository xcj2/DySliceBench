n, k = map(int, input().split())
mod = 10 ** 9 + 7


def cmb_r(n, r):
    n += r - 1
    return cmb(n, r)


def cmb(n, r, mod=10 ** 9 + 7):
    if r < 0 or r > n:
        return 0
    r = min(r, n - r)
    return g1[n] * g2[r] * g2[n - r] % mod


def make_table2(n, mod=10 ** 9 + 7):
    # 元テーブル
    g1 = [0] * (n + 1)
    g1[0] = 1
    g1[1] = 1
    tmp = 1

    for i in range(2, n + 1):
        tmp = tmp * i % mod
        g1[i] = tmp

    # 逆元テーブル
    g2 = [0] * (n + 1)
    g2[-1] = pow(g1[-1], mod - 2, mod)
    tmp = g2[-1]

    for i in range(n - 1, -1, -1):
        tmp = tmp * (i + 1) % mod
        g2[i] = tmp

    return g1, g2


g1, g2 = make_table2(2 * 10 ** 5 + 2)
answer = 0
for i in range(min(n, k) + 1):
    answer += cmb(n, i) * cmb_r(n - i, i) % mod
    answer %= mod

print(answer)