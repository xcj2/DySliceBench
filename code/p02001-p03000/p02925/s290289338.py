from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor
from operator import mul
from functools import reduce


INF = float('inf')
def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
def MSRL(n): return [[int(j) for j in list(S())] for i in range(n)]
mod = 1000000007


n = I()
L = [deque(LI()) for _ in range(n)]

match_set = set()
for i in range(n):
    opponent = L[i][0] - 1
    if i in match_set or opponent in match_set:
        continue
    elif L[opponent][0] - 1 == i:
        L[i].popleft()
        L[opponent].popleft()
        match_set.add(i)
        match_set.add(opponent)


pre_match_set = match_set


cnt = 1
while pre_match_set:
    match_set = set()
    flag = 0
    for j in pre_match_set:
        if not L[j]:
            continue
        opponent = L[j][0] - 1
        if not L[opponent]:
            continue
        if j in match_set or opponent in match_set:
            continue
        if L[opponent][0] - 1 == j:
            flag = 1
            L[j].popleft()
            L[opponent].popleft()
            match_set.add(j)
            match_set.add(opponent)
    if flag:
        cnt += 1
    pre_match_set = match_set



if any([i for i in L]):
    print(-1)
else:
    print(cnt)