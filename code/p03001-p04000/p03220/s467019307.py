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
T, A = MAP()
H = LIST()

tmp = [T-x*0.006 for x in H]
# print(tmp)
y = 100000000
i_tmp = 0
for i, data in enumerate(tmp):
	if abs(data - A) < y:
		y = abs(data - A)
		i_tmp = i+1

print(i_tmp)
