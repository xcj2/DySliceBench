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
import numpy as np
sys.setrecursionlimit(10**8)
input = sys.stdin.readline
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(input())
def inpl(): return list(map(int, input().split()))
def inpl_str(): return list(input().split())

n=inp()
a = inpl()
b = inpl()
ans=0
for i in range(n):
    tmp=a[i] - b[i]
    if tmp >= 0:
        ans += b[i]
    else:
        ans += a[i]
        tmp=-tmp
        temp = a[i + 1] - tmp
        if temp >= 0:
            ans += tmp
            a[i + 1] -= tmp
        else:
            ans += a[i + 1]
            a[i + 1] = 0
print(ans)
    
