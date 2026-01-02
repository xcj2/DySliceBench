import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product
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
F = [LIST() for _ in range(N)]
P = [LIST() for _ in range(N)]

ans = -INF
for i in range(1, 1<<10):
	i = "{:b}".format(i).zfill(10)
	tmp = 0
	for j in range(N):
		cnt = 0
		for k in range(10):
			if int(i[k]) and F[j][k]:
				cnt += 1
		tmp += P[j][cnt]
	ans = max(ans, tmp)
print(ans)
