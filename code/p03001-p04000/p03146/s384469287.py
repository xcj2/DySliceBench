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

s = INT()

dic = defaultdict(int)
dic[s] = 1
for i in range(2, 10000000):
	if s%2 == 0:
		s = s//2
	else:
		s = 3*s + 1
	if dic[s]:
		break
	dic[s] = i+1
print(i)
