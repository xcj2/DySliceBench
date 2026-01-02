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

N = I()
u,v,w = Line(N-1)

c = [[] for _ in range(N)]
for i in range(N-1):
  c[u[i]-1].append([v[i]-1, w[i]])
  c[v[i]-1].append([u[i]-1, w[i]])

d=[-1]*N
v=0
check_visited = [False]*N
check_visited[v] = True
S = [v]
d[v]=0
while S:
  v1 = S.pop()
  for i in c[v1]:
    if check_visited[i[0]] == False:
      check_visited[i[0]] = True
      d[i[0]] = d[v1] + i[1]
      S.append(i[0])

for i in range(N):
  if d[i]%2==0:
    print('0')
  else:
    print('1')