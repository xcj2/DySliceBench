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

def BF(E,s,n):
  inf=float("inf")
  d=[inf for _ in range(n)]
  d[s]=0
  for i in range(n+1):
    for e in E:
      if e[0]!=inf and d[e[1]-1]>d[e[0]-1]+e[2]:
        d[e[1]-1] = d[e[0]-1] + e[2]
    if i==n-1:t=d[-1]
    if i==n and t!=d[-1]:
      return 'loop'
  return d

N,M = II()
E = []
for i in range(M):
  a,b,c = II()
  E.append([a,b,-c])

d = BF(E,0,N)

if d=='loop':
  print('inf')
else:
  print(-d[N-1])