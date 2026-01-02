from collections import defaultdict, deque
import sys
import heapq
import bisect
import math
import itertools
import string
import queue
import copy
import time
sys.setrecursionlimit(10**8)
input = sys.stdin.readline
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(input())
def inpl(): return list(map(int, input().split()))
def inpl_str(): return list(input().split())

n=inp()
p = inpl()
sorted_p = sorted(p)
diff=0
for i in range(n):
    if p[i] != sorted_p[i]:
        diff += 1
if diff == 0 or diff == 2:
    print("YES")
else:
    print("NO")
