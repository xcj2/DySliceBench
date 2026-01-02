# -*- coding: utf-8 -*-
"""
C - Linear Approximation
https://beta.atcoder.jp/contests/abc102/tasks/arc100_a
TLE
"""
import sys
from sys import stdin
input = stdin.readline

from functools import lru_cache
def _solve(arr):
    @lru_cache(maxsize=None)
    def calc_score(n):
        return sum([abs(a-(n+i)) for i, a in enumerate(arr, start=1)])

    ub = max(arr)
    lb = -max(arr)

    while True:
        mid1 = (lb*2 + ub) // 3
        mid2 = (lb + ub*2) // 3
        mid1_score = calc_score(mid1)
        mid2_score = calc_score(mid2)

        if mid2_score > mid1_score:
            ub = mid2
        else:
            lb = mid1
        if abs(ub - lb) <= 4:
            break

    ans = float('inf')
    for b in range(lb, ub+1):
        t = calc_score(b)
        ans = min(ans, t)
    return ans


from statistics import median

def solve(arr):
    def calc_score(n):
        return sum([abs(a-(n+i)) for i, a in enumerate(arr, start=1)])

    array_b = [a-i for i, a in enumerate(arr, start=1)]
    m = median(array_b)
    ans = float('inf')
    for i in range(int(m)-1, int(m)+2):
        ans = min(ans, calc_score(i))
    return ans



def main(args):
    N = int(input())
    arr = [int(a) for a in input().split()]
    ans = solve(arr)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
