#!/usr/bin/env python3

import sys

sys.setrecursionlimit(10**7)


def read_h(typ=int):
    return list(map(typ, input().split()))


def read_v(n, m=1, typ=int):
    return [read_h() if m > 1 else typ(input()) for _ in range(n)]


def solve(arr, positive):
    num_op = 0
    cumul = 0
    #  print('current cumul:', cumul)

    for a in arr:
        cumul += a

        if positive and cumul >= 0:
            num_op += 1 + cumul
            cumul = -1
        elif not positive and cumul <= 0:
            num_op += 1 - cumul
            cumul = 1

        positive = not positive

    return num_op


def main():
    read_h()
    arr = read_h()

    op_plus = solve(arr, True)
    #  print('op plus:', op_plus)
    op_minus = solve(arr, False)
    #  print('op minus:', op_minus)

    print(min(op_plus, op_minus))


if __name__ == '__main__':
    main()
