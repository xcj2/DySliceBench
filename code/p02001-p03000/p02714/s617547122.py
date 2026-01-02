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

a = [i for i in range(n)]

def isOK(mid, point):
    if mid >= point:
        return True
    else:
        return False

#汎用的な二分探索のテンプレ
#条件を満たす最小値（ng,ok）
def binary_search(the_list, point):  # pointより大きい最小値
    ng = -1 #「index = 0」が条件を満たすこともあるので、初期値は -1
    ok = len(the_list) #「index = a.size()-1」が条件を満たさないこともあるので、初期値は a.size()

    #ok と ng のどちらが大きいかわからないことを考慮
    while abs(ok - ng) > 1:
        mid = the_list[(ok + ng) // 2]
        if isOK(mid, point):
            ok = (ok + ng) // 2
        else:
            ng = (ok + ng) // 2
    if ok < len(the_list):
        return the_list[ok], ok
    else:
        return "", ""

def go(a):
    if a == "":
        return False
    return True

for i, first in enumerate(s):
    s_len, t_len = length(first)
    s_list, t_list = rgb_list(first)

    s_i, s_num = binary_search(s_list, i)
    if go(s_i):
        t_i, t_num = binary_search(t_list, i)
        if go(t_num):
            ans += (len(s_list) - s_num) * (len(t_list) - t_num)

for i, first in enumerate(s):
    interval = 1
    while i + 2 * interval < len(s):
        if first != s[i + interval] and s[i + interval] != s[i + 2 * interval] and s[i + 2 * interval] != first:
            ans -= 1
        interval += 1
print(ans)