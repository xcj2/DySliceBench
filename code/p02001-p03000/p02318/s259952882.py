import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
# from fractions import gcd
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from functools import reduce
from bisect import bisect_left, insort_left
from heapq import heapify, heappush, heappop

INPUT = lambda: sys.stdin.readline().rstrip()
INT = lambda: int(INPUT())
MAP = lambda: map(int, INPUT().split())
S_MAP = lambda: map(str, INPUT().split())
LIST = lambda: list(map(int, INPUT().split()))
S_LIST = lambda: list(map(str, INPUT().split()))

sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7


class Levenshtein:
    def init_array(self, str1, str2):
        distance = []
        for i in range(len(str1)+1):
            distance.append([0] * (len(str2) + 1))
            distance[i][0] = i
        for j in range(len(str2)+1):
            distance[0][j] = j
        return distance

    def edit_dist(self, str1, str2, distance):
        dist = [0] * 3
        for i in range(1, len(str1)+1):
            for j in range(1, len(str2)+1):
                dist[0] = distance[i-1][j-1] if str1[i-1] == str2[j-1] else distance[i-1][j-1] + 1
                dist[1] = distance[i][j-1] + 1
                dist[2] = distance[i-1][j] + 1
                distance[i][j] = min(dist)
        return distance[i][j]

    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2
        Levenshtein.distance = self.init_array(str1, str2)
        Levenshtein.dist = self.edit_dist(str1, str2, Levenshtein.distance)


def main():
    s1 = INPUT()
    s2 = INPUT()

    leven = Levenshtein(s1, s2)
    print(leven.dist)


if __name__ == '__main__':
    main()
