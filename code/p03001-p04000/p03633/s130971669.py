# https://atcoder.jp/contests/abc070/tasks/abc070_c

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
    n = input_int()
    T = list(set([input_int() for _ in range(n)]))
    ans = T[0]
    for t in T[1:]:
        ans = ans * t // gcd(ans, t)
    print(ans)

    return


if __name__ == "__main__":
    main()
