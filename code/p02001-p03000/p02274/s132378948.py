import math
import string
import itertools
import fractions
import heapq
import collections
import re
import array
import bisect
import sys
import random
import time
inf = 10**9


class BIT:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i


# def bubble_sort(a):
#     count = 0
#     for i in range(len(a)):
#         for j in range(len(a) - 1, i, -1):
#             if a[j] < a[j - 1]:
#                 a[j - 1], a[j] = a[j], a[j - 1]
#                 count = count + 1
#     return count


def main():
    n = int(input())
    a = list(map(int, input().split()))

    sorted_a = sorted(a)
    map_a = {}
    for i in range(n):
        map_a[sorted_a[i]] = i
    flat_a = list(map(lambda x: map_a[x], a))
    # print(map_a)
    # print(flat_a)

    bit = BIT(n)
    count = 0
    for i in range(n):
        bit.add(flat_a[i] + 1, 1)
        count = count + i + 1 - bit.sum(flat_a[i] + 1)
    print(count)


if __name__ == '__main__':
    main()

# 3 5 2 1 4
# 2 4 1 0 3
#     1|
#     1   1|
#   1|1   1
# 1|1 1   1
# 1 1 1 1|1

