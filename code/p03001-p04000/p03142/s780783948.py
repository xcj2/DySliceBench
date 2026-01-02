from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from copy import deepcopy
from functools import lru_cache, reduce
from math import ceil, floor

import heapq
import itertools
import operator


def get_int():
    return int(input())


def get_str():
    return input().strip()


def get_int_list():
    return [int(i) for i in input().split()]


def get_char_list():
    return list(input().strip())


def main():
    n, m = get_int_list()
    A = []
    B = []
    for _ in range(n - 1 + m):
        a, b = get_int_list()
        A.append(a)
        B.append(b)

    root = (set(A) - set(B)).pop()
    graph = defaultdict(list)
    for a, b in zip(A, B):
        graph[a].append(b)
    known = {root}
    deq = deque([root])
    added = Counter()
    cnt = 0
    while cnt < n - 1 + m:
        parent = deq.popleft()
        children = graph[parent]
        for c in children:
            cnt += 1
            if c in known:
                added[c] += 1
                continue
            known.add(c)
            deq.append(c)
    parents = [0] * n
    deq = deque([root])
    cnt = 1
    while cnt < n:
        parent = deq.popleft()
        children = graph[parent]
        for c in children:
            if added[c] > 0:
                added[c] -= 1
                continue
            parents[c-1] = parent
            cnt += 1
            deq.append(c)
    for parent in parents:
        print(parent)


if __name__ == '__main__':
    main()
