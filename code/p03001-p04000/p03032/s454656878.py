#### import ####
import sys
sys.setrecursionlimit(10**7)
import math
from collections import defaultdict

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

N,K = II()
V = III()

ans = -float('inf')
for i in range(min(N+1,K+1)):
  for j in range(min(N-i+1,K-i+1)):
    V2 = V[:i] + V[N-j:]
    V2.sort()
    temp = sum(V2)
    for k in range(min(K-(i+j),len(V2))):
      if V2[k]<0:
        temp -= V2[k]
    if ans < temp:
      ans = temp
print(ans)