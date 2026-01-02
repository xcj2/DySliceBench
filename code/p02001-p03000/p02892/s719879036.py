import sys
from collections import deque
MAX_INT = int(10e10)
MIN_INT = -MAX_INT
mod = 1000000007
sys.setrecursionlimit(1000000)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

N = I()
s = [[_ for _ in S()] for _ in range(N)]

root = [[] for _ in range(N+1)]
for i in range(N):
  for j in range(N):
    if s[i][j] == "1":
      root[i + 1].append(j + 1)
      root[j + 1].append(i + 1)
      s[j][i] = "0"
#print(root)

ans = -1
for i in range(1, N+1):
  Vnum = [-1 for _ in range(N+1)]
  Vnum[i] = 1

  queue = deque([i])
  while queue:
    #print(queue)
    x = queue.popleft()
    for j in root[x]:
      if Vnum[j] == -1:
        Vnum[j] = Vnum[x] +1
        queue.append(j)
      else:
        if Vnum[j] == Vnum[x] or abs(Vnum[j] - Vnum[x]) > 1:
          break
    else:
      continue
    break
  else:
    ans = max(ans, max(Vnum))

print(ans)