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

def ok(a1, c):
    b1 = c[0][0] - a1
    b2 = c[0][1] - a1
    b3 = c[0][2] - a1

    if len(set([c[1][0] - b1,  c[1][1] - b2,  c[1][2] - b3])) != 1:
        return False
    if len(set([c[2][0] - b1, c[2][1] - b2, c[2][2] - b3])) != 1:
        return False

    return True

def main():
    c = []
    for _ in range(3):
        c.append(list(map(int, input().split())))

    for a1 in range(101):
        if ok(a1, c):
            print(Yes)
            return
    print(No)

if __name__ == '__main__':
    main()
