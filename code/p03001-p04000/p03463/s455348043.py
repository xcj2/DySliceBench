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
YES, NO, Yes, No = "YES", "NO", "Yes", "No"
sys.setrecursionlimit(10**7)

# 4近傍（右, 下, 左, 上）
dy4, dx4 = [0, -1, 0, 1], [1, 0, -1, 0]


def inside(y: int, x: int, H: int, W: int) -> bool: return 0 <= y < H and 0 <= x < W
def ceil(a, b):return (a + b - 1) // b


def solve():
    N, A, B = map(int, input().split())
    if (A - B) % 2 != 0:
        print("Borys")
    else:
        print("Alice")


def main():
    solve()


if __name__ == '__main__':
    main()
