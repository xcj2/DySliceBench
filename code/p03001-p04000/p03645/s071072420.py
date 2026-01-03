import sys
import math
import itertools
import bisect
from copy import copy,deepcopy
from collections import deque,Counter
from decimal import Decimal
def s(): return input()
def i(): return int(input())
def S(): return input().split()
def I(): return map(int,input().split())
def L(): return list(map(int,input().split()))
def l(): return list(map(int,input().split()))
def lcm(a,b): return a*b//math.gcd(a,b)
sys.setrecursionlimit(10 ** 9)
INF = 10**9
mod = 10**9+7

N,M = I()
links = [[] for _ in range(N)]
for i in range(M):
    a,b = I()
    links[a-1].append(b-1)
    links[b-1].append(a-1)
for l1 in links[0]:
    for l2 in links[l1]:
        if l2 == N-1:
            print('POSSIBLE')
            exit()
print('IMPOSSIBLE')