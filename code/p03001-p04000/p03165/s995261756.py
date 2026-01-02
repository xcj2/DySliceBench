import math, string, itertools, fractions, heapq, collections, re, array, bisect, copy, functools, random
import sys
from collections import deque, defaultdict, Counter; from heapq import heappush, heappop
from itertools import permutations, combinations, product, accumulate, groupby
from bisect import bisect_left, bisect_right, insort_left, insort_right
from operator import itemgetter as ig
sys.setrecursionlimit(10 ** 7)
inf = 10 ** 20; INF = float("INF"); ans = ""; tmp = 0; cnt = 0; ansli = []; tmpli = []; candili = []; stillset = set()
eps = 1.0 / 10 ** 10; mod = 10 ** 9 + 7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]; ddn = dd + [(-1, 1), (1, 1), (1, -1), (-1, -1)]; ddn9 = ddn + [(0, 0)]
"""for dx, dy in dd:
        nx = j + dx; ny = i + dy
            if 0 <= nx < w and 0 <= ny < h:"""
def wi(): return list(map(int, sys.stdin.readline().split()))
def wip(): return [int(x) - 1 for x in sys.stdin.readline().split()]#WideIntPoint
def ws(): return sys.stdin.readline().split()
def inp(): return int(sys.stdin.readline())
def st(): return input()
def s_list(): return list(input())
def mi(n): return [wi() for _ in range(n)]#MatrixInt
def num_grid(n): return [[int(i) for i in sys.stdin.readline().split()[0]] for _ in range(n)]#NumberGrid
def mip(n): return [wip() for _ in range(n)]
def ms(n): return [ws() for _ in range(n)]
def grid(n): return [s_list() for _ in range(n)]

# LCS
def main():
    s = st()
    t = st()
    slen = len(s)
    tlen = len(t)
    # まず，長さを求める
    # dp[i][j]=(sをi文字目、tをj文字目までみた時の最長共通部分列の長さ)とする
    dp = [[0 for j in range(tlen + 1)] for i in range(slen + 1)]
    # slenはSの長さ、tlenはTの長さとする
    for i in range(1, slen + 1):
        for j in range(1, tlen + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1  # この文字は使ったほうがいい
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  # どっちかの最後の1文字は使わない

    # dp[slen][tlen]が求める長さ

    # 文字復元
    length = dp[slen][tlen]
    i = slen
    j = tlen
    ans = ["" for _ in range(length)]
    while length > 0:
        if s[i - 1] == t[j - 1]:
            ans[length - 1] = s[i - 1]
            i -= 1
            j -= 1
            length -= 1
        elif dp[i][j] == dp[i - 1][j]: # i文字目が無くても同じ，i文字目は使わない
            i -= 1
        else:
            j -= 1
    print("".join(ans))

if __name__ == '__main__':
    main()