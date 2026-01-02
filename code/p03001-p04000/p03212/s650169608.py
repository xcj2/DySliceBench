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

    n = int(input())
    str_n = str(n)
    #print(str_n)
    ngs = ['3','5','7']
    #a = list(product(ngs, repeat=len(str_n)))
    #print(a)
    ans = ''
    count = 0
    for i in range(1,len(str_n)+1):
        for j in list(product(ngs, repeat=i)):
            #print(j)
            for k in j:
                ans += k
            #print(ans)
            ngs_and_ans = set(ngs) & set(ans)
            if int(ans) <= n and len(ngs_and_ans) == 3:
                count += 1
            ans = ''
    print(count)


if __name__ == '__main__':
    main()
