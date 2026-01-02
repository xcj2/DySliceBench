#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**8)
from bisect import bisect_left
from itertools import product
import math
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def LI_(): return list(map(lambda x: int(x)-1, input().split()))
def LF(): return list(map(float, input().split()))
def LC(): return [c for c in input().split()]
def LLI(n): return [LI() for _ in range(n)]
def NSTR(n): return [input() for _ in range(n)]

def array2d(N, M, initial=0):
    return [[initial]*M for _ in range(N)]

def copy2d(orig, N, M):
    ret = array2d(N, M)
    for i in range(N):
        for j in range(M):
            ret[i][j] = orig[i][j]
    return ret


INF = float("inf")
MOD = 10**9 + 7


def main():
    N, K = MAP()
    A = LI()

    if K == 0:
        print(max(A))
        return

    # 決め打ち二分探索
    left = 0
    right = 10**9+7
    # for i in range(100):
    while right - left > 1:
        mid = (right + left) // 2
        count = 0
        for a in A:
            count += int(math.ceil(a / mid))-1
        if count <= K:
            right = mid
        else:
            left = mid
    # print(int(math.ceil(left)))
    print(right)

    return


if __name__ == '__main__':
    main()
