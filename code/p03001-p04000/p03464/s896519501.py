import sys
from collections import defaultdict, Counter
from itertools import product, groupby, count, permutations, combinations
from math import pi, sqrt, floor
from collections import deque
from bisect import bisect, bisect_left, bisect_right
from string import ascii_lowercase
from functools import lru_cache, reduce
from operator import xor
from heapq import heappush, heappop
INF = float("inf")
sys.setrecursionlimit(10**7)

# 4近傍（右, 下, 左, 上）
dy4, dx4 = [0, -1, 0, 1], [1, 0, -1, 0]


def inside(y: int, x: int, H: int, W: int) -> bool: return 0 <= y < H and 0 <= x < W
def ceil(a, b):return (a + b - 1) // b


def up(a, b):
    s = ceil(a, b)
    for i in range(s - 1, s + 3):
        if i * b > a:
            return i * b


def check(n, A):
    for a in A:
        n = (n // a) * a
    return n == 2


def solve(A):


    if A[-1] != 2:
        return [-1]

    min_a, max_a = 2, 3
    for a in A[::-1][1:]:
        if a > max_a:
            return [-1]
        else:
            max_a = up(max_a, a) - 1

        if a >= min_a:
            min_a = a
        else:
            min_a = ceil(min_a, a) * a

    if min_a > max_a:
        return [-1]
    return min_a, max_a

def solve2(A):
    min_a = INF
    max_a = 0
    for i in range(0, 100):
        if check(i, A):
            min_a = min(min_a, i)
            max_a = max(max_a, i)

    if min_a == INF or max_a == 0:
        return [-1]
    return min_a, max_a

def solve3(A):
    # [low, high)
    min_a = INF
    max_a = 0

    low, high = 0, int(1e14) - 1
    while high - low > 1:
        middle = (low + high) // 2
        if check(middle, A):
            min_a = middle
            low = middle
        else:
            high = middle

    low, high = 0, int(1e14) - 1
    while high - low > 1:
        middle = (low + high) // 2
        if check(middle, A):
            max_a = middle
            high = middle
        else:
            low = middle

    if min_a == INF or max_a == 0:
        return [-1]
    return min_a, max_a

def main():
    K = int(input())
    A = list(map(int, input().split()))

    print(*solve(A))



if __name__ == '__main__':
    main()
