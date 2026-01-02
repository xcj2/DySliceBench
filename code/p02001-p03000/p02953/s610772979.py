#### import ####
import sys
import math
from collections import defaultdict

#### 設定 ####
sys.setrecursionlimit(10**7)

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

N = I()
H = III()
H[0] -= 1
for i in range(1,N):
  if H[i]<H[i-1]:
    print('No')
    exit()
  if H[i]-1>=H[i-1]:
    H[i]-=1
print('Yes')