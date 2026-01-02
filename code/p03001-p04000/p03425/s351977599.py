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
S = [input() for _ in range(N)]

count = defaultdict(int)

for s in S:
	if s[0] in ["M", "A", "R", "C", "H"]:
		count[s[0]] += 1

ans = 0
for a, b, c in combinations(count.values(), 3):
	ans += a*b*c
print(ans)
