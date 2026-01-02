# -*- coding: utf-8 -*-
"""
C - Stones
https://atcoder.jp/contests/tenka1-2019-beginner/tasks/tenka1_2019_c

"""
import sys


def solve(N, S):
    black = 0
    white = S.count('.')
    ans = float('inf')

    for s in S + ' ':
        ans = min(ans, black+white)
        if s == '#':
            black += 1
        else:
            white -= 1
    return ans


def __solve(N, S):
    ans1 = 0
    prev = '@'
    for s in S:
        if prev == '#' and s == '.':
            ans1 += 1
            prev = '#'
        else:
            prev = s
    return ans1


def main(args):
    N = int(input())
    S = input()
    ans = solve(N, S)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
