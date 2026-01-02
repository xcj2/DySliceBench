#### import ####
import sys
import math
from collections import defaultdict

#### 設定 ####
sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

#### 定数 ####
mod = 10**9 + 7

#### 読み込み ####
def I(): return int(input())
def II(): return map(int, input().split())
def III(): return list(map(int, input().split()))
def Line(N):
    read_all = [tuple(map(int, input().split())) for _ in range(N)]
    return map(list,zip(*read_all))

#################

from itertools import combinations

N = I()
S = ['0']*N
x = [0]*5
for i in range(N):
    S[i] = str(input())
    if S[i].startswith('M'):
        x[0] += 1
    elif S[i].startswith('A'):
        x[1] += 1
    elif S[i].startswith('R'):
        x[2] += 1
    elif S[i].startswith('C'):
        x[3] += 1
    elif S[i].startswith('H'):
        x[4] += 1

ans = 0
A = list(combinations(range(5),3))
for a in A:
    ans += x[a[0]]*x[a[1]]*x[a[2]]

print(ans)