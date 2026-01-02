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

n, m = wi()
a = wi()
bc = mi(m)
a.sort()
de = deque()
for i in range(n):
    de.append(a[i])
bc.sort(key=ig(1), reverse=True)

for i in range(m):

    def isOK(mid):
        if de[mid] > bc[i][1]:
            return False
        else:
            return True


    #汎用的な二分探索のテンプレ
    def binary_search(n):
        ok = -1 #「index = 0」が条件を満たすこともあるので、初期値は -1
        ng = n #「index = a.size()-1」が条件を満たさないこともあるので、初期値は a.size()

        #ok と ng のどちらが大きいかわからないことを考慮
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2

            if isOK(mid):
                ok = mid
            else:
                ng = mid
        return ok

    bs = binary_search(n)

    if bs + 1 > bc[i][0]:
        ans += bc[i][0] * bc[i][1]
        for _ in range(bc[i][0]):
            de.popleft()
    else:
        ans += (bs + 1) * bc[i][1]
        for _ in range(bs + 1):
            de.popleft()
    n -= min(bs + 1, bc[i][0])

ans += sum(de)

print(ans)