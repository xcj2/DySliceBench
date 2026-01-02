import math
import sys


def Knight():
    def check(d):
        if (d[0] + d[1]) % 3 or d[0] < 0 or d[1] < 0:
            print(0)
            sys.exit()
    d = list(map(int, input().split()))
    check(d)

    x = d[0]
    y = d[1]
    diff = x - y if x > y else y - x  # aとbの回数の差
    d2 = [x - diff, y - diff * 2] if x < y else [x - diff * 2, y - diff]
    r = d2[0] // 3

    def cmb(n, r, mod):
        if (r < 0 or r > n):
            return 0
        r = min(r, n-r)
        return g1[n] * g2[r] * g2[n-r] % mod

    mod = 10**9+7  # 出力の制限
    N = x if x > y else y
    g1 = [1, 1]  # 元テーブル
    g2 = [1, 1]  # 逆元テーブル
    inverse = [0, 1]  # 逆元テーブル計算用テーブル

    for i in range(2, N + 1):
        g1.append((g1[-1] * i) % mod)
        inverse.append((-inverse[mod % i] * (mod//i)) % mod)
        g2.append((g2[-1] * inverse[-1]) % mod)

    a = cmb(r*2+diff, r, mod)

    print(a)


Knight()
