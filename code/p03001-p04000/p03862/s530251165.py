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

N, x = MAP()
a = LIST()
count = 0
def reduce_candy(i): # iとi+1のキャンディを減らす
	global count
	if sum_near[i] <= x: # 減らす必要なし
		pass 
	elif sum_near[i] - a[i] <= x: # 左のボックスから全部減らすと条件クリアの場合
		if not i == 0:
			sum_near[i-1] -= sum_near[i] - x
		a[i] -= sum_near[i] - x
		count += sum_near[i] - x
		sum_near[i] = x
	else: # 左のボックスと右のボックスの両方から取り出す必要あり
		if not i == 0:
			sum_near[i-1] -= a[i]
		sum_near[i] -= a[i]
		count += a[i]
		a[i] = 0
		a[i+1] -= sum_near[i] - x
		count += sum_near[i] - x
		sum_near[i] = x
sum_near = []
for i in range(N-1):
	sum_near.append(a[i] + a[i+1])

for i in range(N-2, -1, -1):
	reduce_candy(i)
	# print(count)
	# print(sum_near)
print(count)