import sys

# import bisect
# from collections import Counter, deque, defaultdict
# import copy
# from heapq import heappush, heappop, heapify
# from fractions import gcd
# import itertools
# from operator import attrgetter, itemgetter

# import math

# from numba import jit

# from scipy import
# import numpy as np
# import networkx as nx

# import matplotlib.pyplot as plt

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


class SegmentTree:

    def __init__(self, array, operator, identity):
        self.identity = identity
        self.operator = operator

        self.array_size = len(array)
        self.tree_height = (self.array_size - 1).bit_length()
        self.tree_size = 2 ** (self.tree_height + 1)
        self.leaf_start_index = 2 ** self.tree_height
        self.tree = [self.identity] * self.tree_size

        for i in range(self.array_size):
            x = 1 << (ord(array[i]) - 96)
            self.tree[self.leaf_start_index + i] = x

        for i in range(self.leaf_start_index - 1, 0, -1):
            self.tree[i] = self.operator(self.tree[i << 1], self.tree[i << 1 | 1])

    def update(self, index, val):
        x = 1 << (ord(val) - 96)

        cur_node = self.leaf_start_index + index
        self.tree[cur_node] = x

        while cur_node > 1:
            self.tree[cur_node >> 1] = self.operator(self.tree[cur_node], self.tree[cur_node ^ 1])
            cur_node >>= 1

    def query(self, begin, end):
        if begin < 0:
            begin = 0
        elif begin > self.array_size:
            return self.identity
        if end > self.array_size:
            end = self.array_size
        elif end < 1:
            return self.identity

        res = self.identity

        left = begin + self.leaf_start_index
        right = end + self.leaf_start_index

        while left < right:
            if left & 1:
                res = self.operator(res, self.tree[left])
                left += 1

            if right & 1:
                right -= 1
                res = self.operator(res, self.tree[right])

            left >>= 1
            right >>= 1

        return res


def main():
    from operator import or_
    n = int(input())
    s = input()
    q = int(input())

    seg = SegmentTree(s, or_, 0)

    for i in range(q):
        q1, q2, q3 = readline().split()
        q1, q2 = int(q1), int(q2)
        if q1 == 1:
            seg.update(q2-1, q3.rstrip("\n"))
        else:
            q3 = int(q3)
            print(bin(seg.query(q2-1, q3)).count("1"))


if __name__ == '__main__':
    main()
