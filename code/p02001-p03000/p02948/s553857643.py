import sys
import math
import itertools
import bisect
from copy import copy
from collections import deque,Counter
from decimal import Decimal
def s(): return input()
def i(): return int(input())
def S(): return input().split()
def I(): return map(int,input().split())
def L(): return list(input().split())
def l(): return list(map(int,input().split()))
def lcm(a,b): return a*b//math.gcd(a,b)
sys.setrecursionlimit(10**9)
INF = 10**9
mod = 10**9+7
import heapq

N,M = I()
L = [l() for _ in range(N)]
A = deque([])
B = deque([])
L.sort()
ans = 0
for a,b in L:
    A.append(a)
    B.append(b)
q = []
heapq.heapify(q)
for i in range(1,M+1):
    for j in range(len(A)):
        if A[0] > i:
            break
        else:
            A.popleft()
            heapq.heappush(q,B.popleft()*-1)
    if q:
        ans += heapq.heappop(q)*-1
print(ans)