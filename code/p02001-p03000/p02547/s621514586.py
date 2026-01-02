import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
import decimal
from decimal import Decimal
decimal.getcontext().prec = 10

from heapq import heappush, heappop, heapify
import math
from math import gcd
import itertools as it
import collections
from collections import deque 

def inp():
    return int(input())
def inpl():
    return list(map(int, input().split()))
def _debug(obj):
    print(obj, file=sys.stderr)

# ---------------------------------------

n = inp()
cnt = 0
mx = 0
for i in range(n):
    d1, d2 = inpl()
    if d1 == d2:
        cnt += 1
    else:
        cnt = 0
    mx = max(mx, cnt)

if mx >= 3:
    print("Yes")
else:
    print("No")

