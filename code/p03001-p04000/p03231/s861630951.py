# https://atcoder.jp/contests/agc028/tasks/agc028_a

import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]
# Greatest Common Divisor(Euclidean algorithm)


def gcd(x: int, y: int) -> int:
    if x < y:
        x, y = y, x
    while y > 0:
        r = x % y
        x, y = y, r
    return x


# Least Common Multiple
def lcm(x: int, y: int) -> int:
    _gcd = gcd(x, y)
    return (x * y) // _gcd


def main():
    n, m = input_int_list()
    _gcd = gcd(m, n)
    size = lcm(m, n)
    S = input()
    T = input()
    if S[::n // _gcd] == T[::m // _gcd]:
        print(size)
    else:
        print(-1)


if __name__ == "__main__":
    main()
