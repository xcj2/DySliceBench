import sys

import numpy as np
import math, string, itertools, fractions, heapq, collections, re, array, bisect, copy, functools, random
from collections import deque, defaultdict, Counter
from heapq import heappush, heappop
from itertools import permutations, combinations, product, accumulate, groupby
from bisect import bisect_left, bisect_right, insort_left, insort_right
from operator import itemgetter as ig
sys.setrecursionlimit(10 ** 7)
inf = 10 ** 20
INF = float("INF")
mod = 10 ** 9 + 7
"""dd = [(-1, 0), (0, 1), (1, 0), (0, -1)];
ddn = dd + [(-1, 1), (1, 1), (1, -1), (-1, -1)];
ddn9 = ddn + [(0, 0)]
for dx, dy in dd:
        nx = j + dx; ny = i + dy
            if 0 <= nx < w and 0 <= ny < h:"""

def wi(): return list(map(int, sys.stdin.readline().split()))
def wip(): return [int(x) - 1 for x in sys.stdin.readline().split()]  # WideIntPoint
def ws(): return sys.stdin.readline().split()
def si(): return int(sys.stdin.readline())  # SingleInt
def ss(): return input()
def hi(n): return [si() for _ in range(n)]
def hs(n): return [ss() for _ in range(n)]  # HeightString
def s_list(): return list(input())
def mi(n): return [wi() for _ in range(n)]  # MatrixInt
def mip(n): return [wip() for _ in range(n)]
def ms(n): return [ws() for _ in range(n)]
def num_grid(n): return [[int(i) for i in sys.stdin.readline().split()[0]] for _ in range(n)]  # NumberGrid
def grid(n): return [s_list() for _ in range(n)]


def main():
    n, m = map(int,input().split())

    G = defaultdict(list)
    for i in range(m):
        a, b = map(int,input().split())
        G[a].append(b)
        G[b].append(a)
    #print(G)

    # stackは次の探索候補?
    # visitedはもう探索済み
    stack = [(1, [1])]
    ans = 0
    # stack(次の探索候補)が空になるまで回す
    while stack:
        # xは今見ているノード
        x, visited = stack.pop()

        if len(visited) == n:
            ans += 1

        # vは今見ているノードの隣接ノード
        for v in G[x]:
            if v in visited:
                continue
            stack.append((v, visited + [v]))

    print(ans)


if __name__ == '__main__':
    main()
