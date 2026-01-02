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

N, C = MAP()
D = [LIST() for _ in range(C)]
c = [LIST() for _ in range(N)]

group0 = []
group1 = []
group2 = []
for i in range(N):
	for j in range(N):
		if (i+j)%3 == 0:
			group0.append(c[i][j]-1)
		elif (i+j)%3 == 1:
			group1.append(c[i][j]-1)
		elif (i+j)%3 == 2:
			group2.append(c[i][j]-1)
# print(group0)
# print(group1)
# print(group2)

color_0 = []
inv_0 = {}
for i in range(C):
	tmp = 0
	for item0 in group0:
		tmp += D[item0][i]
	color_0.append((tmp, i))
	inv_0[i] = tmp
color_0 = sorted(color_0)[0:3]
color_0_lis = [x[1] for x in color_0]

color_1 = []
inv_1 = {}
for i in range(C):
	tmp = 0
	for item1 in group1:
		tmp += D[item1][i]
	color_1.append((tmp, i))
	inv_1[i] = tmp
color_1 = sorted(color_1)[0:3]
color_1_lis = [x[1] for x in color_1]

color_2 = []
inv_2 = {}
for i in range(C):
	tmp = 0
	for item2 in group2:
		tmp += D[item2][i]
	color_2.append((tmp, i))
	inv_2[i] = tmp
color_2 = sorted(color_2)[0:3]
color_2_lis = [x[1] for x in color_2]
# print(color_0)
# print(color_0_lis)
# print(color_1)
# print(color_1_lis)
# print(color_2)
# print(color_2_lis)
ans = INF
for i in color_0_lis:
	for j in color_1_lis:
		for k in color_2_lis:
			tmp = 0
			if i == j or j == k or k == i:
				continue
			else:
				tmp += inv_0[i]
				tmp += inv_1[j]
				tmp += inv_2[k]
				ans = min(ans, tmp)
print(ans)
