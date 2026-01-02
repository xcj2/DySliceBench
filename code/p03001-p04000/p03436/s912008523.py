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

H,W = IL()
grid = [list(S()) for i in range(H)]

ans = 0
for i in range(H):
  for j in range(W):
    if grid[i][j] == ".":
      ans += 1

data = [[MAX_INT]*W for i in range(H)]

d = deque()
d.append((1, 0, 0)) # (cnt, h, w)
while d:
  cnt, h, w = d.popleft()
  if data[h][w] > cnt:
    data[h][w] = cnt
    for i,j in ((-1,0), (0,-1),(1,0),(0,1)):
      if 0 <= h+i < H and 0 <= w+j < W:
        if grid[h+i][w+j] == ".":
          d.append((cnt+1, h+i, w+j))
if data[-1][-1] == MAX_INT:
  print(-1)
else:
  print(ans - data[-1][-1])