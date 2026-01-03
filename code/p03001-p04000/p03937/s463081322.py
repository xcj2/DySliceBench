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

H,W = II()
A = [list(map(str, input())) for _ in range(H)]
for i in range(H):
  A[i].append('?')
A.append(['?']*(W+1))

i=0;j=0
A[i][j]='.'
while 1:
  if i==H-1 and j==W-1:
    break
  if A[i+1][j]=='#':
    A[i+1][j]='.'
    i +=1
    continue
  if A[i][j+1]=='#':
    A[i][j+1]='.'
    j +=1
    continue
  print('Impossible')
  exit()

ans = 'Possible'
for i in range(H):
  for j in range(W):
    if A[i][j]=='#':
      ans = 'Impossible'
print(ans)