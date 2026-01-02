import sys
import numpy as np


def input():
    return sys.stdin.readline()[:-1]


def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)


def factorize(n):
    res = dict()
    for i in range(2, int(np.sqrt(n)) + 10):
        if n % i:
            continue
        res.setdefault(i, 0)
        while (n % i == 0):
            n //= i
            res[i] += 1
    if n != 1:
        res.setdefault(n, 1)
    return res


def solve():
    a, b = map(int, input().split())
    n = gcd(a, b)
    print(len(factorize(n))+1)


if __name__ == "__main__":
    solve()
