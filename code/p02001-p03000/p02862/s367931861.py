#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)

MOD = 1000000007  # type: int

def get_z(y, x): # y/x (mod 1000000007)
    inv_x = pow(x, MOD - 2, MOD)
    return y * inv_x % MOD

def comb_mod(n, k):
    if n == 0:
        return 0
    k = min(k, n - k)
    a = 1
    b = 1
    for i in range(k):
        a = a * (n - i) % MOD
        b = b * (i + 1) % MOD
    ret = get_z(a, b)
    return ret


def solve(X: int, Y: int):
    d = X - Y
    s = (X + Y) // 3
    x = (s + d) // 2
    y = (s - d) // 2
    if (X + Y) % 3 or (s + d) % 2 or x < 0 or y < 0 \
            or x * 2 + y != X or x + y * 2 != Y:
        print(0)
        return
    ret = comb_mod(x + y, min(x, y))
    print(ret)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    X = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    solve(X, Y)

if __name__ == '__main__':
    main()
