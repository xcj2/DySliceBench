import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect_left
from heapq import heappush, heappop

def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
MOD = 10 ** 9 + 7

N, K = MAP()
td = [LIST() for _ in range(N)]
td.sort(key=lambda x:-x[1])

q = []
v = set()
s = 0
for t, d in td[:K]:
	s += d
	if t in v:
		heappush(q, d)
	else:  # その種類で最大(最初)のものは以後取り出さないのでヒープに追加しない
		v.add(t)
s += len(v) ** 2  # +種類ボーナス
ans = s

for t, d in td[K:]:  # 残りについて取り替えるか取り替えないか決める
	if t not in v and len(q) != 0:
		z = heappop(q)
		s += d + 2*len(v)+1-z  # 種類ボーナスと満足ボーナスの差分
		v.add(t)
		ans = max(ans, s)
print(ans)
