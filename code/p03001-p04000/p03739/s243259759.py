# -*- coding: utf-8 -*-
"""
https://abc059.contest.atcoder.jp/tasks/arc072_a
WA
"""
import sys
from sys import stdin
input = stdin.readline


def check_sign(n):
    if n > 0:
        return 1
    elif n < 0:
        return -1
    else:
        return 0


def solve(A):
    p_ans = 0
    n_ans = 0
    i_ans = 0

    # 最初をプラス側に振った場合の解
    total = A[0]
    prev_sign = check_sign(total)
    if prev_sign == 0:
        p_ans += 1
        total += 1
        prev_sign = 1

    for a in A[1:]:
        total += a
        sign = check_sign(total)
        if sign == 0:
            total -= prev_sign
            p_ans += 1
        elif prev_sign != sign:
            prev_sign = sign
        else:
            p_ans += (abs(total) + 1)
            if prev_sign < 0:
                total = 1
                prev_sign = 1
            else:
                total = -1
                prev_sign = -1

    # 最初をマイナス側に振った場合の解
    total = A[0]
    prev_sign = check_sign(total)
    if prev_sign == 0:
        n_ans += 1
        total -= 1
        prev_sign = -1

    for a in A[1:]:
        total += a
        sign = check_sign(total)
        if sign == 0:
            total -= prev_sign
            n_ans += 1
        elif prev_sign != sign:
            prev_sign = sign
        else:
            n_ans += (abs(total) + 1)
            if prev_sign < 0:
                total = 1
                prev_sign = 1
            else:
                total = -1
                prev_sign = -1

    # 反転させてからスタートする
    total = A[0]
    prev_sign = check_sign(total)
    if prev_sign == 0:
        i_ans += 1
        total += 1
        prev_sign = 1
    else:
        i_ans += (abs(total) + 1)
        if prev_sign > 0:
            prev_sign = -1
            total = -1
        else:
            prev_sign = 1
            total = 1

    for a in A[1:]:
        total += a
        sign = check_sign(total)
        if sign == 0:
            total -= prev_sign
            i_ans += 1
        elif prev_sign != sign:
            prev_sign = sign
        else:
            i_ans += (abs(total) + 1)
            if prev_sign < 0:
                total = 1
                prev_sign = 1
            else:
                total = -1
                prev_sign = -1

    return min(p_ans, n_ans, i_ans)


def main(args):
    n = int(input())
    A = [int(x) for x in input().split()]
    ans = solve(A)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
