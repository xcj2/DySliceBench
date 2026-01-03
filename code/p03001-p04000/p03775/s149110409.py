# -*- coding: utf-8 -*-
"""
https://beta.atcoder.jp/contests/abc057/tasks/abc057_c

"""
import sys
from sys import stdin
input = stdin.readline


def calc_divisors(N):
    ans = [N]
    for i in range(2, int(N**0.5)+1):
        if N % i == 0:
            ans.append(i)
            # if N // i != i:
            #     ans.append(N//i)
    ans.sort()
    return ans


def solve(N):
    min_ans = float('inf')
    divs = calc_divisors(N)

    for d in divs:
        A = d
        B = N // d
        A_len = len(str(A))
        B_len = len(str(B))
        AB_len = max(A_len, B_len)
        min_ans = min(min_ans, AB_len)
    return min_ans


def main(args):
    N = int(input())
    ans = solve(N)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
