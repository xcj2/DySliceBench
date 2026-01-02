# https://atcoder.jp/contests/panasonic2020/tasks/panasonic2020_c

from decimal import Decimal

import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    a, b, c = input_int_list()
    sqrt_a = Decimal(a)**Decimal("0.5")
    sqrt_b = Decimal(b)**Decimal("0.5")
    sqrt_c = Decimal(c)**Decimal("0.5")
    if sqrt_a + sqrt_b < sqrt_c:
        print("Yes")
    else:
        print("No")
    return


if __name__ == "__main__":
    main()
