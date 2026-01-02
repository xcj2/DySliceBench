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

H,W,K = II()
from itertools import product

if W==1:
  if K==1:
    print(1)
  else:
    print(0)
  exit()

#i番目のrowを通過後j+1にいる場合の数
dp = [[0]*W for _ in range(H+1)]
dp[0][0] = 1
for i in range(1,H+1):
  for j in range(W):
    if 0<=j-1:
      a = list(product(['+','-'],repeat=W-1))
      counter = 0
      for a1 in a:
        if a1[j-1]!= '+':
          continue
        else:
          for k in range(1,W-1):
            if a1[k] == '+' and a1[k-1] == '+':
              break
            else:
              if k == W-2:
                counter += 1
      dp[i][j] += dp[i-1][j-1]*counter
      dp[i][j] %= mod
      
    if W-1>=j+1:
      a = list(product(['+','-'],repeat=W-1))
      counter = 0
      for a1 in a:
        if a1[j]!= '+':
          continue
        else:
          for k in range(1,W-1):
            if a1[k] == '+' and a1[k-1] == '+':
              break
            else:
              if k == W-2:
                counter += 1
      dp[i][j] += dp[i-1][j+1]*counter
      dp[i][j] %= mod

    a = list(product(['+','-'],repeat=W-1))
    counter = 0
    for a1 in a:
      if j <= W-2:
        if a1[j] == '+':
          continue
      if j-1>=0:
        if a1[j-1] == '+':
          continue
      for k in range(1,W-1):
        if a1[k] == '+' and a1[k-1] == '+':
          break
        else:
          if k==W-2:
            counter += 1
    dp[i][j] += dp[i-1][j]*counter
    dp[i][j] %= mod

print(dp[H][K-1])