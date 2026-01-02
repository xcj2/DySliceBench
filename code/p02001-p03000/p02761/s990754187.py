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
keta = [-1]*(N)
for i in range(M):
    s,c = I()
    if keta[s-1] == -1 or keta[s-1] == c:
        keta[s-1] = c
    else:
        print(-1)
        exit()
if keta[0] == -1 and len(keta) != 1:
    keta[0] = 1
for i in range(N):
    if keta[i] == -1:
        keta[i] = '0'
    else:
        keta[i] = str(keta[i])
if ''.join(keta) != str(int(''.join(keta))):
    print(-1)
else:
    print(''.join(keta))
