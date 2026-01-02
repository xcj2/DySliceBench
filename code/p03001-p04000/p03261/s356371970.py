import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import Counter, deque
from collections import defaultdict
from itertools import combinations, permutations, accumulate, groupby, product
from bisect import bisect_left,bisect_right
from heapq import heapify, heappop, heappush
from math import floor, ceil
from operator import itemgetter
from copy import deepcopy
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def LI2(): return [int(input()) for i in range(n)]
def MXI(): return [[LI()]for i in range(n)]
inf = 10**17
mod = 10**9 + 7

n=I()
words=[input().rstrip() for i in range(n)]
u=len(list(set(words)))
if u!=n:
    print("No")
    sys.exit()
for i in range(n-1):
    if words[i][-1]!=words[i+1][0]:
        print("No")
        sys.exit()
print("Yes")