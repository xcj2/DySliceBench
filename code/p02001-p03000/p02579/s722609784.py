import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, radians, degrees, log2, gcd
from itertools import accumulate, permutations, combinations, combinations_with_replacement, product, groupby
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left, insort, insort_left
from heapq import heappush, heappop
from functools import reduce, lru_cache
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def TUPLE(): return tuple(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = 10**6#float('inf')
mod = 10 ** 9 + 7 
#mod = 998244353
from decimal import *
#import numpy as np
#decimal.getcontext().prec = 10


def main():
	H, W = MAP()
	Ch, Cw = MAP()
	Dh, Dw = MAP()
	S = [input() for _ in range(H)]

	cnt = [[INF]*W for _ in range(H)]
	cnt[Ch-1][Cw-1] = 0

	dy = [1, 0, -1, 0, 1, 1, -1, -1, 2, 2, 2, 1, 0, -1, -2, -2, -2, -2, -2, -1, 0, 1, 2, 2]
	dx = [0, -1, 0, 1, 1, -1, -1, 1, 0, -1, -2, -2, -2, -2, -2, -1, 0, 1, 2, 2, 2, 2, 2, 1]

	q = deque([(Ch-1, Cw-1, 0)])
	while q:
		y, x, c = q.popleft()
		if cnt[y][x] != c:
			continue
		flg = True
		for i in range(24):
			if i == 4 and flg:
				break
			ny = y + dy[i]
			nx = x + dx[i]
			if ny < 0 or nx < 0 or H <= ny or W <= nx:
				continue
			elif i < 4:
				if S[ny][nx] == "." and c < cnt[ny][nx]:
					cnt[ny][nx] = c
					q.appendleft((ny, nx, c))
				elif S[ny][nx] == "#":
					flg = False
			elif 4 <= i and S[ny][nx] == "." and c+1 < cnt[ny][nx]:
				cnt[ny][nx] = c+1
				q.append((ny, nx, c+1))


	if cnt[Dh-1][Dw-1] == INF:
		print(-1)
	else:
		print(cnt[Dh-1][Dw-1])

if __name__ == '__main__':
	main()