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

dx = [0, 1, 0, -1, 1, 1, -1, -1]
dy = [1, 0, -1, 0, 1, -1, 1, -1]
def DFS(i, j):
	global w, h
	for x in range(8):
		nx = j + dx[x]
		ny = i + dy[x]
		if 0 <= nx <= w-1 and 0 <= ny <= h-1 and c[ny][nx]==1:
			c[ny][nx] = 0
			DFS(ny, nx)

ans = []
while 1:
	w, h = MAP()
	if [w, h] == [0, 0]:
		break
	c = [LIST() for _ in range(h)]

	count = 0
	for i in range(h):
		for j in range(w):
			if c[i][j] == 1:
				c[i][j] = 0
				DFS(i, j)
				count += 1
	ans.append(count)

for i in ans:
	print(i)

