import sys
import bisect
import math
import itertools


# \n
def input():
    return sys.stdin.readline().rstrip()


def dist(Z1, Z2):
    x1, y1 = Z1
    x2, y2 = Z2
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


def middle(X1, X2, X3):
    x1, y1 = X1
    x2, y2 = X2
    x3, y3 = X3

    alpha = x1 - x2
    beta = y1 - y2
    gamma = x2 - x3
    delta = y2 - y3

    div = (alpha * delta - beta * gamma) * 2
    if div == 0:
        return 60000, 60000

    div = 1 / div
    upper = x1 ** 2 + y1 ** 2 - x2 ** 2 - y2 ** 2
    lower = x2 ** 2 + y2 ** 2 - x3 ** 2 - y3 ** 2

    a = div * (delta * upper - beta * lower)
    b = div * (-gamma * upper + alpha * lower)

    return a, b


def main():
    NN, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()

    def cmb(n, r, mod):
        if (r < 0 or r > n):
            return 0
        r = min(r, n - r)
        return g1[n] * g2[r] * g2[n - r] % mod

    mod = 10 ** 9 + 7  # 出力の制限
    N = 10 ** 5 + 10
    g1 = [1, 1]  # 元テーブル
    g2 = [1, 1]  # 逆元テーブル
    inverse = [0, 1]  # 逆元テーブル計算用テーブル

    for i in range(2, N + 1):
        g1.append((g1[-1] * i) % mod)
        inverse.append((-inverse[mod % i] * (mod // i)) % mod)
        g2.append((g2[-1] * inverse[-1]) % mod)

    sup = 0
    inf = 0

    for i in range(NN - K + 1):
        c = cmb(NN-i-1, K - 1, mod)

        inf += c*A[i]
        inf %=mod
        sup += c*A[-i-1]
        sup %=mod

    print((sup-inf)%mod )


if __name__ == "__main__":
    main()
