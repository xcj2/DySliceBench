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

N, A, B, C, D, E = [INT() for _ in range(6)]
trans = [A, B, C, D, E]
num_city = [N, 0, 0, 0, 0, 0]
time = 0
for i in range(5):
	# print(num_city)
	if not i==4:
		if trans[i] == 1:
			tmp = 1
		else:
			tmp = num_city[i]%trans[i]
		num_city[i+1] = N-tmp
		if N-tmp <= trans[i+1]*((time+(ceil(num_city[i]/trans[i])))-(i+1)):
			num_city[i+1] = 0
		else:
			num_city[i+1] -= trans[i+1]*((time+(ceil(num_city[i]/trans[i])))-(i+1))
		num_city[i+1] += tmp
		time += ceil(num_city[i]/trans[i])
		num_city[i] = 0
	else:
		time += ceil(num_city[4]/E)
print(time)