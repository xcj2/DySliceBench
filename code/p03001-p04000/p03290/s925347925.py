#!/usr/bin/env python3

import sys

sys.setrecursionlimit(10**7)

# Override `input` function because `stdin.readline()` is 10x faster than built-in `input()`
input = sys.stdin.readline


def read_h(typ=int):
    return list(map(typ, input().split()))


def read_v(n, m=1, typ=int):
    return [read_h(typ) if m > 1 else typ(input()) for _ in range(n)]


def solve(d, g, pc):
    min_num = 100 * d + 1
    for i in range(2**d):
        num = 0
        score = 0
        offset = -1
        for j in range(d):
            if (i >> j) & 1:
                # Solve full problems
                # print('i = {}, j = {}'.format(i, j))
                p, c = pc[j]
                # print('p = {}, c = {}'.format(p, c))
                num += p
                score += 100 * (j + 1) * p + c
                # print('num = {}, score = {}'.format(num, score))
            else:
                offset = j
                # print('offset:', offset)

        if score < g:
            # Solve incomplete problems
            short = 100 * (offset + 1)
            # print('short:', short)
            need = (g - score + short - 1) // short
            if need >= pc[offset][0]:
                continue
            # print('need:', need)
            num += need
            # print('need added:', num)

        min_num = min(min_num, num)
        # print('min num:', min_num)

    return min_num


def main():
    d, g = read_h()
    pc = read_v(d, m=2)
    # print(pc)

    num = solve(d, g, pc)
    print(num)


if __name__ == '__main__':
    main()
