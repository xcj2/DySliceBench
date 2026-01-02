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
    T = "AKIHABARA"
    if len(S) > len(T):
        return False
    if S.replace("A", "") != T.replace("A", ""):
        return False

    s, t = 0, 0
    while s < len(S) and t < len(T):
        if S[s] == T[t]:
            s, t = s + 1, t + 1
        elif S[s] != T[t] and T[t] == "A":
            t += 1
        else:
            return False

    if s == len(S):
        return True
    else:
        return False


def main():
    S = input()
    print("YES" if solve(S) else "NO")


if __name__ == '__main__':
    main()
