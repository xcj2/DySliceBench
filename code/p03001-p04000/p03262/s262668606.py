# https://atcoder.jp/contests/abc109/tasks/abc109_c

import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def gcd(x: int, y: int) -> int:
    if x < y:
        x, y = y, x
    while y > 0:
        r = x % y
        x, y = y, r
    return x


def main():
    n, x = input_int_list()
    X = input_int_list()
    ans = abs(x - X[0])
    for i in range(1, n):
        ans = gcd(ans, abs(x - X[i]))
    print(ans)

    return


if __name__ == "__main__":
    main()
