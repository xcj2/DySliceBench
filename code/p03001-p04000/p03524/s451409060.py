import sys
from collections import defaultdict, Counter
from itertools import product, groupby, count, permutations, combinations
from math import pi, sqrt, ceil, floor
from collections import deque
from bisect import bisect, bisect_left, bisect_right
from string import ascii_lowercase
INF = float("inf")
sys.setrecursionlimit(10**7)

# 4近傍（右, 下, 左, 上）
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]


def inside(y: int, x: int, H: int, W: int) -> bool: return 0 <= y < H and 0 <= x < W


def solve(S):
    a = S.count("a")
    b = S.count("b")
    c = S.count("c")
    a, b, c = list(sorted([a, b, c], reverse=True))
    if (a == b == c) or (a - 1 == b == c) or (a - 1 == b - 1 == c):
        return True
    return False


def main():
    S = input()
    print("YES" if solve(S) else "NO")


if __name__ == '__main__':
    main()
