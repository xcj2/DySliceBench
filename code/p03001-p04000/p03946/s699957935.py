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

N, T = MAP()
A = LIST()
# B = [max(A[i+1:N])-A[i] for i in range(N-1)] # O(N^2)時間かかる
# print(B)
min_ = INF
B = []
for i in A:
	B.append(i-min_)
	# print(min_)
	if min_ > i:
		min_ = i
# print(B)
print(B.count(max(B)))