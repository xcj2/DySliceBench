import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, gcd
from itertools import accumulate, permutations, combinations, product, groupby, combinations_with_replacement
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


while 1:
	w, h = MAP()
	if w == 0 and h == 0:
		exit()

	c = [LIST() for _ in range(h)]

	cnt = 0
	check = [[0]*w for _ in range(h)]

	dy = (1, 1, 0, -1, -1, -1, 0, 1)
	dx = (0, -1, -1, -1, 0, 1, 1, 1)

	for y in range(h):
		for x in range(w):
			if check[y][x] == 0 and c[y][x] == 1:
				cnt += 1
				check[y][x] = cnt
				q = deque([(y, x)])
				while q:
					ny, nx = q.popleft()
					for k in range(8):
						ky = ny + dy[k]
						kx = nx + dx[k]
						if 0 <= ky < h and 0 <= kx < w and check[ky][kx] == 0 and c[ky][kx] == 1:
							check[ky][kx] = cnt
							q.append((ky, kx))

	print(cnt)
