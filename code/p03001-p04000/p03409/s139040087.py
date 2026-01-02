import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from heapq import heappop, heappush, heapify, heappushpop
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits

def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
MOD = 10 ** 9 + 7

N = INT()
ab = [LIST() for _ in range(N)]
cd = [LIST() for _ in range(N)]

ab.sort(key=lambda x:(-x[1], -x[0]))
cd.sort(key=lambda x:(x[0], x[1]))

ans = 0
for c, d in cd:  # 青の点
	for i in range(len(ab)):  # 赤の点
		if c > ab[i][0] and d > ab[i][1]:  # マッチング
			# print(ab[i], c, d)
			ab.pop(i)
			ans += 1
			break
print(ans)
