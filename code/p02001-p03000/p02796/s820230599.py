import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import accumulate, permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect

def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
MOD = 10 ** 9 + 7

N = INT()
XL = [LIST() for _ in range(N)]

range_lis = [(x[0]-x[1], x[0]+x[1]) for x in XL]
# print(range_lis)

range_lis.sort(key=lambda x:x[1])

tmp = range_lis[0][1]
ans = 1
for i in range(1, N):
	if range_lis[i][0] >= tmp:
		tmp = range_lis[i][1]
		ans += 1
print(ans) 
