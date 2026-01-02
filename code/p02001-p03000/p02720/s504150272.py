import math, string, itertools, fractions, heapq, collections, re, array, bisect, copy, functools, random
import sys
from collections import deque, defaultdict, Counter; from heapq import heappush, heappop
from itertools import permutations, combinations, product, accumulate, groupby
from bisect import bisect_left, bisect_right, insort_left, insort_right
from operator import itemgetter as ig
sys.setrecursionlimit(10 ** 7)
inf = 10 ** 20; INF = float("INF"); ans = 0; tmp = 0; ansli = []; tmpli = []; candili = []
eps = 1.0 / 10 ** 10; mod = 10 ** 9 + 7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]; ddn = dd + [(-1, 1), (1, 1), (1, -1), (-1, -1)]; ddn9 = ddn + [(0, 0)]
"""for dx, dy in dd:
        nx = j + dx; ny = i + dy
            if 0 <= nx < w and 0 <= ny < h:"""
def wi(): return list(map(int, sys.stdin.readline().split()))
def wip(): return [int(x) - 1 for x in sys.stdin.readline().split()]#WideIntPoint
def ws(): return sys.stdin.readline().split()
def i(): return int(sys.stdin.readline())
def s(): return input()
def hi(n): return [i() for _ in range(n)]
def hs(n): return [s() for _ in range(n)]#HeightString
def mi(n): return [wi() for _ in range(n)]#MatrixInt
def mip(n): return [wip() for _ in range(n)]
def ms(n): return [ws() for _ in range(n)]

k = i()
lunlun_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
tmp_list = lunlun_list
tmp_tmp_list = []
cnt = 9
def lunlun(y):
    x = y[-1]
    if x == "0":
        tmp_tmp_list.append(y + "0")
        tmp_tmp_list.append(y + "1")
        return 2
    elif x == "9":
        tmp_tmp_list.append(y + "8")
        tmp_tmp_list.append(y + "9")
        return 2
    else:
        x = int(x)
        tmp_tmp_list.append(y + str(x - 1))
        tmp_tmp_list.append(y + str(x))
        tmp_tmp_list.append(y + str(x + 1))
        return 3

while len(lunlun_list) < k:
    for tmp in tmp_list:
        cnt += lunlun(str(tmp))
        if cnt >= k:
            break
    tmp_list = tmp_tmp_list
    lunlun_list += tmp_list
    tmp_tmp_list = []

lunlun_list = [int(i) for i in lunlun_list]
lunlun_list.sort()

print(lunlun_list[k - 1])