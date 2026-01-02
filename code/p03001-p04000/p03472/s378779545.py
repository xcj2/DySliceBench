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

N,H = I()
A = []
B = []
for i in range(N):
    a,b = I()
    A.append(a)
    B.append(b)
B.sort(reverse=True)
huru = max(A)
cnt = 0
for i in range(N):
    if B[i] < huru:
        break
    H -= B[i]
    cnt += 1
    if H <= 0:
        print(cnt)
        exit()
print(cnt+math.ceil(H/huru))