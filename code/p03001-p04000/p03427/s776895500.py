# -*- coding: utf-8 -*-
"""
A - Digit Sum 2
https://atcoder.jp/contests/agc021/tasks/agc021_a

"""
import sys


def calc_digit_sum(s):
    return sum([int(ch) for ch in s])

def solve(N):
    l = len(N)
    all_nine = True
    res = []
    for i, n in enumerate(N[::-1], start=1):
        if i != l:
            if n != '9':
                all_nine = False
            res.append('9')
        else:
            res.append(str(int(n)-1))

    if all_nine or l == 1:
        return calc_digit_sum(N)
    return calc_digit_sum(res)



def main(args):
    N = input()
    ans = solve(N)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
