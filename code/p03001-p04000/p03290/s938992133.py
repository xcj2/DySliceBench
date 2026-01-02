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

D, G = MAP()
pc = [LIST() for _ in range(D)]
count_min = 1000000000
for i in range(1<<D):
	sum_ = 0
	count = 0
	i = list("{:b}".format(i).zfill(D))
	# print(i)
	for j in range(D):
		if i[j] == '1':  # j = '1' なら全部加える
			sum_ += (j+1)*100*pc[j][0] + pc[j][1]
			count += pc[j][0]
	if sum_ >=  G:
		if count < count_min:
			# print("更新", count_min,"->",count)
			count_min = count
	else:  # 中途半端にとる
		for j in range(D-1, -1, -1):
			if i[j] == '0':  # G - sum_ : 残りのポイント
				num = ceil((G-sum_)/((j+1)*100))
				# print(num)
				if num > pc[j][0]:
					count = 1000000000
					break
				count += ceil((G-sum_)/((j+1)*100))
				break
		if count < count_min:
			# print("更新", count_min,"->",count)
			count_min = count

print(count_min)
