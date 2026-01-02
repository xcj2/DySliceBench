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

N, Q = MAP()
S = list(input())
lr = [LIST() for _ in range(Q)]

lis = [0]*N

for i, x in enumerate(S):
    if (i == N-1):
        break
    else:
        if x == 'A' and S[i + 1] == 'C':
            lis[i+1] = lis[i]+1
        else:
            lis[i+1] = lis[i]


for i in range(Q):
    print(lis[lr[i][1]-1]-lis[lr[i][0]-1])
