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

s = s()[::-1]
n = len(s)
# dp[i][j] := 先頭 i + 1 文字として考えられるもののうち，13 で割ったあまりが j であるものの数
dp = [[0 for _ in range(13)] for _ in range(n)]
# 初期値
if s[0] == "?":
    for j in range(10):
        dp[0][j] = 1
else:
    dp[0][int(s[0])] = 1

# dp[i + 1][(j + x * d) % 13] += dp[i][j]，前のやつの余りj（j=0～12に集約されている）を用いて，次のやつを考えていく，
# xを10倍していくが，値が大きくなりすぎるとまずいので，mod13を毎回とる（結果は変わらない）
x = 10
for i in range(n - 1):
    if s[i + 1] == "?":
        start = 0
        end = 10
    else:
        start = int(s[i + 1])
        end = int(s[i + 1]) + 1
    for d in range(start, end):
        for j in range(13):
            dp[i + 1][(j + x * d) % 13] += dp[i][j]
            dp[i + 1][(j + x * d) % 13] %= mod
    x = x * 10 % 13

print(dp[n - 1][5] % mod)