import sys
import math
MAX_INT = int(10e15)
MIN_INT = -MAX_INT
mod = 1000000007
sys.setrecursionlimit(1000000)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

def tami(n, cnt):
  aoki_visited[n] = True
  aoki[n] = cnt
  for x in edge[n]:
    if aoki_visited[x] == False:
      tami(x, cnt+1)

def tami2(n, cnt):
  choku_visited[n] = True
  if cnt <= aoki[n]:
    choku[n] = cnt
    for x in edge[n]:
      if choku_visited[x] == False:
        tami2(x, cnt+1)

N, u, v = IL()
ab = [IL() for _ in range(N-1)]

aoki = [0]*(N+1)
aoki_visited = [False]*(N+1)
choku = [0]*(N+1)
choku_visited = [False]*(N+1)

edge = [[] for _ in range(N+1)]
for a,b in ab:
  edge[a].append(b)
  edge[b].append(a)

ans = 0
aoki[v] = MAX_INT
tami(v, 0)
tami2(u, 0)
#print(aoki)
#print(choku)

for i in range(N+1):
  if choku[i] == 0 and i != u:
    continue
  if aoki[i] > choku[i]:
    ans = max(ans, aoki[i] - 1)

print(ans)
