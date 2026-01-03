import sys
from collections import defaultdict, Counter
from itertools import product, groupby, count, permutations, combinations
from math import pi, sqrt, ceil, floor
from collections import deque
from bisect import bisect, bisect_left, bisect_right
from string import ascii_lowercase
from functools import lru_cache, reduce
from operator import xor
INF = float("inf")
sys.setrecursionlimit(10**7)

# 4近傍（右, 下, 左, 上）
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]


def inside(y: int, x: int, H: int, W: int) -> bool: return 0 <= y < H and 0 <= x < W


def solve(N, l):
    a, b = min(l), max(l)
    if b - a > 1:
        return False
    if a == b:
        if a == N - 1:
            return True
        return N >= (a * 2)

    num_a = l.count(a)

    return num_a < b and num_a + 2 * (b - num_a) <= N


def main():
    N = int(input())
    a_list = list(map(int, input().split()))
    print("Yes" if solve(N, a_list) else "No")

if __name__ == '__main__':
    main()
