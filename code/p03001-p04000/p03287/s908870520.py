import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, log10
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

N, M = MAP()
A = LIST()

A_acc = list(accumulate(A))
A_acc_mod = [x%M for x in A_acc]

dic = defaultdict(int)
for i in A_acc_mod:
	dic[i] += 1

ans = 0
for val in dic.values():
	if val >= 2:
		ans += val*(val-1)//2
ans += dic[0]
print(ans)
