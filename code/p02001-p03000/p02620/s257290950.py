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

D = INT()
C = LIST()
s = [LIST() for _ in range(D)]
t = [INT() for _ in range(D)]

## 1回最終スコアを計算する
score = [0]*26
last = [0]*26
now = 0
for i in range(D):  # i+1日目
    score[t[i]-1] += s[i][t[i]-1]
    last[t[i]-1] = i+1
    for j in range(26):
        score[j] -= C[j]*(i+1-last[j])

now = sum(score)
M = INT()

ans = [0]*M
for i in range(M):  # nowからの差分を考える
    d, q = MAP()  # q:更新後
    d -= 1
    q -= 1
    c = t[d]-1  # c:更新前
    t[d] = q+1
    last_c = 0
    last_q = 0
    score_c = 0
    score_q = 0
    for j in range(D):
        if t[j]-1 == c:
            last_c = j+1
            score_c += s[j][c]
        elif t[j]-1 == q:
            last_q = j+1
            score_q += s[j][q]
        score_c -= C[c] * (j+1 - last_c)
        score_q -= C[q] * (j+1 - last_q)
    now += -score[c]-score[q]+score_c+score_q
    score[c] = score_c
    score[q] = score_q
    ans[i] = now

print(*ans, sep="\n")
