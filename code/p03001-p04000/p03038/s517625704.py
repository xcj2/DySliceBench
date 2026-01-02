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

N,M = II()
A = III()
B,C = Line(M)

a = []
for i in range(N):
  a.append([1,A[i]])
for i in range(M):
  a.append([B[i],C[i]])

#a.sort(key=lambda x:x[1],reverse=True)
a.sort(key=lambda x:-x[1])
counter = 0
ans = 0

for i in range(N+M):
  if counter + a[i][0] >= N:
    ans += a[i][1]*(N-counter)
    break
  else:
    counter += a[i][0]
    ans += a[i][1]*a[i][0]

print(ans)