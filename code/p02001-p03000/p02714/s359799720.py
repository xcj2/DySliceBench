import bisect, collections, copy, heapq, itertools, math, string
from functools import reduce
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = I()
S = S()
R_num = [n for n, v in enumerate(S) if v == 'R']
G_num = [n for n, v in enumerate(S) if v == 'G']
B_num = [n for n, v in enumerate(S) if v == 'B']


cnt = 0
for r in R_num:
    for g in G_num:
        x = r + g
        if x % 2 == 0:
            if x // 2 in B_num:
                cnt += 1
for g in G_num:
    for b in B_num:
        x = g + b
        if x % 2 == 0:
            if x // 2 in R_num:
                cnt += 1
for r in R_num:
    for b in B_num:
        x = r + b
        if x % 2 == 0:
            if x // 2 in G_num:
                cnt += 1

ans = len(R_num) * len(G_num) * len(B_num) - cnt
print(ans)