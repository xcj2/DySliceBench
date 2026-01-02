import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, gcd
from itertools import accumulate, permutations, combinations, product, groupby
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from heapq import heappush, heappop
from functools import reduce
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

N = INT()
S = input()

nR = S.count("R")
nG = S.count("G")
nB = S.count("B")
ans = nR*nG*nB
for i in range(N):  # 開始 index
	for j in range(1, N//2+1):  # 幅
		if i+2*j >= N:
			continue
		a, b, c = S[i], S[i+j], S[i+2*j]
		if a != b and b != c and c != a:
			ans -= 1
print(ans)
