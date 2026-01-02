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

#x以上で最小のyの倍数
def min_mult(x,y):
    if x%y==0:
        return x
    else:
        return x + (y-x%y)

N = I()
C,S,F = Line(N-1)

ans = []

for i in range(N-1):
    temp = S[i]+C[i]
    for j in range(i+1,N-1):
        temp = min_mult(max(temp,S[j]),F[j]) + C[j]
    ans.append(temp)

ans.append(0)
for i in range(N):
    print(ans[i])