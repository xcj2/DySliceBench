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
    T = list("AKIHABARA")
    l = [0, 4, 6, 8]
    for i in range(len(l) + 1):
        for j in combinations(l, r=i):
            t = T[:]
            for x in j[::-1]:
                t.pop(x)
            if S == "".join(t):
                return True
    return False


def main():
    S = input()
    print("YES" if solve(S) else "NO")


if __name__ == '__main__':
    main()
