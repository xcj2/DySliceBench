import math, string, itertools, fractions, heapq, collections, re, array, bisect, copy, functools, random
import sys
from collections import deque, defaultdict, Counter; from heapq import heappush, heappop
from itertools import permutations, combinations, product, accumulate, groupby
from bisect import bisect_left, bisect_right, insort_left, insort_right
from operator import itemgetter as ig
sys.setrecursionlimit(10 ** 7)
inf = 10 ** 20; INF = float("INF"); ans = 0; tmp = 0; cnt = 0; ansli = []; tmpli = []; candili = []; stillset = set()
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
def s_list(): return list(input())
def hi(n): return [i() for _ in range(n)]
def hs(n): return [s() for _ in range(n)]#HeightString
def mi(n): return [wi() for _ in range(n)]#MatrixInt
def num_grid(n): return [[int(i) for i in sys.stdin.readline().split()[0]] for _ in range(n)]#NumberGrid
def mip(n): return [wip() for _ in range(n)]
def ms(n): return [ws() for _ in range(n)]
def grid(n): return [s_list() for _ in range(n)]


r_list= []
g_list = []
b_list = []
def length(t):
    if t == "R":
        return len(g_list), len(b_list)
    elif t == "G":
        return len(b_list), len(r_list)
    else:
        return len(r_list), len(g_list)

def rgb_list(t):
    if t == "R":
        return g_list, b_list
    elif t == "G":
        return b_list, r_list
    else:
        return r_list, g_list
n = i()
s = s()

for i, t in enumerate(s):
    if t == "R":
        r_list.append(i)
    elif t == "G":
        g_list.append(i)
    else:
        b_list.append(i)

rgb = ["R", "G", "B"]
s_start = 0
t_start = 0
r_start = 0
g_start = 0
b_start = 0

for i, first in enumerate(s):
    a1 = 0
    a2 = 0
    if first == "R":
        for g_i in range(g_start, len(g_list)):
            if i < g_list[g_i]:
                g_start = g_i
                a1 = 1
                break
        for b_i in range(b_start, len(b_list)):
            if i < b_list[b_i]:
                b_start = b_i
                a2 = 1
                break
        if a1 == 1 and a2 == 1:
            ans += (len(g_list) - g_start) * (len(b_list) - b_start)

    elif first == "G":
        for r_i in range(r_start, len(r_list)):
            if i < r_list[r_i]:
                r_start = r_i
                a1 = 1
                break
        for b_i in range(b_start, len(b_list)):
            if i < b_list[b_i]:
                b_start = b_i
                a2 = 1
                break
        if a1 == 1 and a2 == 1:
            ans += (len(r_list) - r_start) * (len(b_list) - b_start)

    else:
        for g_i in range(g_start, len(g_list)):
            if i < g_list[g_i]:
                g_start = g_i
                a1 = 1
                break
        for r_i in range(r_start, len(r_list)):
            if i < r_list[r_i]:
                r_start = r_i
                a2 = 1
                break
        if a1 == 1 and a2 == 1:
            ans += (len(g_list) - g_start) * (len(r_list) - r_start)

for i, first in enumerate(s):
    interval = 1
    while i + 2 * interval < len(s):
        if first != s[i + interval] and s[i + interval] != s[i + 2 * interval] and s[i + 2 * interval] != first:
            ans -= 1
        interval += 1
print(ans)