#!/usr/bin/python3

from collections import defaultdict, Counter
from itertools import product, groupby, count, permutations, combinations
from math import pi, sqrt
from collections import deque
from bisect import bisect, bisect_left, bisect_right
from string import ascii_lowercase
from functools import lru_cache
import sys
sys.setrecursionlimit(10000)
INF = float("inf")
YES, Yes, yes, NO, No, no = "YES", "Yes", "yes", "NO", "No", "no"
dy4, dx4 = [0, 1, 0, -1], [1, 0, -1, 0]


def inside(y, x, H, W):
    return 0 <= y < H and 0 <= x < W


def ok(A, B, S):
    if len(S) != A + B + 1:
        return False
    if S.count("-") != 1:
        return False

    a, b = S.split("-")
    if len(a) != A or len(b) != B:
        return False

    return True


def main():
    A, B = map(int, input().split())
    S = input()
    if ok(A, B, S):
        print(Yes)
    else:
        print(No)


if __name__ == '__main__':
    main()
