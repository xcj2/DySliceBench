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

N,M = II()
a,b = Line(M)

can_visit = defaultdict(list)
for i in range(M):
  can_visit[a[i]-1].append(b[i]-1)
  can_visit[b[i]-1].append(a[i]-1)
from itertools import permutations
road = list(permutations([i for i in range(N)]))
counter = 0
for r in road:
  if r[0]!=0:
    continue
  temp = 0
  check_visited = [False]*N
  check_visited[0] = True
  for i in r[1:]:
    if (i in can_visit[temp]) and (check_visited[i]==False):
      temp = i
      check_visited[i] = True
      if check_visited == [True]*N:
        counter += 1
        break
    else:
      break
print(counter)