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

N, A, B, C = MAP()
l = [INT() for _ in range(N)]

def dfs(cur, a, b, c):
    if cur == N: # 最初の1つを入れた分の10*3を引く
        return abs(a-A) + abs(b-B) + abs(c-C) - 30 if min(a, b, c) > 0 else INF
    ret0 = dfs(cur+1, a, b, c)  # 使わない
    ret1 = dfs(cur+1, a+l[cur], b, c) + 10  # Aに加える
    ret2 = dfs(cur+1, a, b+l[cur], c) + 10  # Bに加える
    ret3 = dfs(cur+1, a, b, c+l[cur]) + 10  # Cに加える
    return min(ret0, ret1, ret2, ret3)
print(dfs(0, 0, 0, 0))
