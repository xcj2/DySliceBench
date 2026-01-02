import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, gcd
from itertools import accumulate, permutations, combinations, product, groupby, combinations_with_replacement
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from heapq import heappush, heappop
from functools import reduce

def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

N = INT()

def warshall_floyd(v_count: int, matrix: list) -> list:
    for i in range(v_count):
        for j, c2 in enumerate(row[i] for row in matrix):
            for k, (c1, c3) in enumerate(zip(matrix[j], matrix[i])):
                if c1 > c2+c3:
                    matrix[j][k] = c2+c3
    return matrix

A = [LIST() for _ in range(N)]
dist_matrix = warshall_floyd(N, deepcopy(A))

ans = 0
for i, j in combinations(range(N), 2):
    if A[i][j] != dist_matrix[i][j]:
        print(-1)
        break
    for k in range(N):
        if i == k or j == k:
            continue
        if A[i][k] + A[k][j] == A[i][j]:
            break
    else:
        ans += A[i][j]
else:
    print(ans)
