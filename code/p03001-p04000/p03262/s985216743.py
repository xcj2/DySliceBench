# -*- coding: utf-8 -*-
"""
C - Skip
https://atcoder.jp/contests/abc109/tasks/abc109_c

"""
import sys

from bisect import bisect_right, bisect_left

def solve(N, X, points):
    def divisor(N):
        divisors = set()
        for i in range(1, int(N**0.5)+1):
            if N % i == 0:
                divisors.add(i)
                divisors.add(N // i)
        return sorted(divisors)

    left, right = float('inf'), float('inf')
    l = bisect_left(points, X)
    if l:
        left = points[l-1]
    r = bisect_right(points, X)
    if r != len(points):
        right = points[r]

    gaps = [abs(X-p) for p in points]
    candidates = divisor(min(abs(left-X), abs(right-X)))
    while True:
        c = candidates.pop()
        if all([g%c==0 for g in gaps]):
            return c


def main(args):
    N, X = map(int, input().split())
    points = sorted(map(int, input().split()))
    ans = solve(N, X, points)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
