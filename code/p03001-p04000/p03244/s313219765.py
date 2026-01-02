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

n = INT()
v = LIST()

v_odd = [v[i] for i in range(n) if i % 2 == 1]
v_even = [v[i] for i in range(n) if i % 2 == 0]

count_odd = Counter(v_odd)
count_even = Counter(v_even)

if count_odd.most_common()[0][0] != count_even.most_common()[0][0]:
	print(int(n/2-count_odd.most_common()[0][1] + n/2 - count_even.most_common()[0][1]))
else:
	if len(count_odd) == 1 and len(count_even) == 1:
		print(int(n/2))
	else:
		if len(count_odd) == 1:
			print(int(n/2 - count_even.most_common()[1][1]))
		elif len(count_even) == 1:
			print(int(n/2 - count_odd.most_common()[1][1]))
		else:
			tmp1 = int(n/2-count_odd.most_common()[1][1] + n/2 - count_even.most_common()[0][1])
			tmp2 = int(n/2-count_odd.most_common()[0][1] + n/2 - count_even.most_common()[1][1])
			print(min(tmp1, tmp2))