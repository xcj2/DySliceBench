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
def L(): return list(map(int,input().split()))
def l(): return list(map(int,input().split()))
def lcm(a,b): return a*b//math.gcd(a,b)
sys.setrecursionlimit(10 ** 9)
INF = 10**9
mod = 10**9+7

S = deque(list(s()))
cnt = 0
N = len(S)
for i in range(N):
    N = len(S)
    if N <= 1:
        break
    if S[0] == 'x':
        if S[N-1] == 'x':
            S.pop()
            S.popleft()
        else:
            cnt += 1
            S.popleft()
    else:
        a = S[0]
        if S[N-1] == 'x':
            cnt += 1
            S.pop()
        elif S[N-1] == a:
            S.pop()
            S.popleft()
        else:
            print(-1)
            exit()
print(cnt)