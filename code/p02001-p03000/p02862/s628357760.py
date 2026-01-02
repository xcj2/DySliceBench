import sys


def mulmod(x, y, p=10**9 + 7):
    return x * y % p


def combmod(n, k, p=10**9 + 7):
    from functools import reduce
    k = min(k, n - k)
    x = reduce(mulmod, range(n - k + 1, n + 1), 1)
    y = reduce(mulmod, range(1, k + 1), 1)
    return x * pow(y, p - 2, p) % p


def solve(string):
    x, y = map(int, string.split())
    m0, m1 = min(x, y), max(x, y)
    if (x + y) % 3 > 0 or m1 / m0 > 2:
        return "0"
    n = (x + y) // 3
    return str(combmod(n, m0 - n))


if __name__ == '__main__':
    print(solve(sys.stdin.read()))
