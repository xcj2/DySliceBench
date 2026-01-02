#!/usr/bin/env python3

import sys

sys.setrecursionlimit(10**7)

# Override `input` function because `stdin.readline()` is 10x faster than built-in `input()`
input = sys.stdin.readline


def read_h(typ=int):
    return list(map(typ, input().split()))


def read_v(n, m=1, typ=int):
    return [read_h(typ) if m > 1 else typ(input()) for _ in range(n)]


def main():
    S, = read_h(typ=str)
    ints = [int(i) for i in S]

    for i in range(2**3):
        ops = ['+'] * 3
        for j in range(3):
            if ((i >> j) & 1):
                ops[j] = '-'

        #  print(ints)
        #  print(ops)

        s = ints[0]
        for op, i in zip(ops, ints[1:]):
            if op == '+':
                s += i
            else:
                s -= i

        if s == 7:
            ans = ''.join([str(i) + op for i, op in zip(ints, ops + [''])] + ['=7'])
            print(ans)
            return


if __name__ == '__main__':
    main()
