#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**8)
import math
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def ZIP(n): return [LIST() for _ in range(n)]
def NSTR(n): return [input() for _ in range(n)]


INF = float("inf")
MOD = 10**9 + 7


def main():
    N, K = MAP()
    A = LIST()

    if K == 0:
        print(max(A))
        return

    # X決め打ち二分探索
    left = 0
    right = 10**9+7
    for i in range(100):
        # while right - left > 1.0e-6:
        mid = (right + left) / 2
        count = 0
        for a in A:
            count += int(math.ceil(a / mid))-1
        if count <= K:
            right = mid
        else:
            left = mid
    print(int(math.ceil(left)))

    return


if __name__ == '__main__':
    main()
