import sys
import re
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

n, k = MAP()

h = LIST()

dp = [INF] * n
dp[0] = 0

for i, hi in enumerate(h):
    if i == 0:
        continue
    s = i-k if i-k >= 0 else 0
    dp[i] = min([dpk + abs(hi-hk) for dpk, hk in zip(dp[s:i], h[s:i])])

print(dp[-1])
