import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, log2
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

N, M = MAP()

ks = [LIST() for _ in range(M)]

p = LIST()

ans = 0
for i in range(1<<N):  # スイッチの状態を全探索
	i = list("{:b}".format(i).zfill(N))
	flag = True
	for j, lis in enumerate(ks):
		lis = lis[1:]
		tmp = 0
		for l in lis:
			if i[l-1] == '1':
				tmp += 1
		if tmp % 2 != p[j]:
			flag = False
			break
	if flag:
		ans += 1
print(ans)