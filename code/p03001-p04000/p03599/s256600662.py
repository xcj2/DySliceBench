from heapq import heappush, heappop
from itertools import permutations, accumulate, combinations
from math import pi, ceil, floor
import numpy as np
from collections import defaultdict, deque
from operator import itemgetter
from bisect import bisect_left, bisect_right, insort_left, insort_right
import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10 ** 6)
# MOD = 10 ** 9 + 7
# INF = float("inf")


def total_check(sugar, water, lim):
    if sugar + water <= lim:
        return True
    else:
        return False


def concentration(sugar, water, lim_sugar):
    if sugar / (sugar + water) <= lim_sugar / (lim_sugar + 100):
        return True
    else:
        return False


def main():
    a, b, c, d, lim_sugar, lim = map(int, input().split())
    water_list = []
    for i in range(lim // (100 * a) + 1):
        for j in range(lim // (100 * b) + 1):
            if i == 0 and j == 0: continue
            w = 100 * i * a + 100 * j * b
            if w > lim: continue
            water_list.append(w)
    water_list = sorted(list(set(water_list)))

    sugar_list = []
    for i in range(lim // c + 1):
        for j in range(lim // d + 1):
            s = i * c + j * d
            if s > lim: continue
            sugar_list.append(s)
    sugar_list = sorted(list(set(sugar_list)))

    c = 0
    ans = (100 * a, 0)
    for w in water_list:
        for s in sugar_list:
            if total_check(s, w, lim) and concentration(s, w, lim_sugar):
                if c < s * 100 / (s + w):
                    c = s * 100 / (s + w)
                    ans = (s + w, s)
    print(*ans)


if __name__ == '__main__':
    main()