MOD = 10 ** 9 + 7


def power_expo(x, y):
    """Returns x^y.

    <https://qiita.com/Yaruki00/items/fd1fc269ff7fe40d09a6>

    結局, 組み込み関数の `pow()` のほうが速そう. 第3引数でmodもできる.
    """
    if y == 0:
        return 1
    elif y % 2 == 0:
        return power_expo(x, y // 2) ** 2 % MOD
    else:
        return power_expo(x, y // 2) ** 2 * x % MOD


def combinations_mod(n, r, mod=1000000007):
    """Returns nCr in mod."""
    combs = 1
    for i, j in zip(range(n - r + 1, n + 1), range(1, r + 1)):
        combs = combs % mod * i % mod * pow(j, mod - 2, mod) % mod
    return combs


def main():
    x, y = [int(x) for x in input().split()]
    if (x + y) % 3 != 0:
        return 0
    summ = (x + y) // 3     # d + r
    diff = x - y  # d - r
    if summ % 2 != diff % 2:
        return 0
    d = (summ + diff) // 2  # Down
    r = (summ - diff) // 2  # Right
    if d < 0 or r < 0:
        return 0
    chosen = min(d, r)

    patterns = combinations_mod(summ, chosen)

    return patterns


if __name__ == '__main__':
    print(main())

# やはり難しい，再び解説。割り算のときは mod 10^9+7 が厄介。
# とりあえず，割る方は 10^9+5 乗して掛ければいいらしい。
# でかい累乗, pow() なら間に合うな. Python3 1310 ms; Pypy3 457 ms.
