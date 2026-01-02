import math
import itertools
from collections import deque
import bisect
import heapq

def IN(): return int(input())
def sIN(): return input()
def lIN(): return list(input())
def MAP(): return map(int,input().split())
def LMAP(): return list(map(int,input().split()))
def TATE(n): return [input() for i in range(n)]
ans = 0

def bfs(sx,sy):
    d = [[-1] * w for i in range(h)]
    MAX = 0

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    que = deque([])
    que.append((sx, sy))#スタート座標の記録
    d[sx][sy] = 0#スタートからスタートへの最短距離は0

    while que:#中身がなくなるまで
        p = que.popleft()
       
        for m in range(4):#現在地から4方向の移動を考える
            nx = p[0] + dx[m]
            ny = p[1] + dy[m]

            if 0 <= nx < h and 0 <= ny < w:
              if maze[nx][ny] != "#" and d[nx][ny] == -1:
                que.append((nx, ny))#↑格子点からでない＆壁でない＆まだ通ってない
                d[nx][ny] = d[p[0]][p[1]] + 1

    for k in range(h):
      MAX = max(max(d[k]),MAX)
      
    return MAX

h, w = map(int, input().split())
maze = [lIN() for i in range(h)]

for i in range(h):#sx座標指定0~h-1
  for j in range(w):#sy座標指定0~w-1
    if maze[i][j] == '.':
      ans = max(bfs(i,j),ans)
      
print(ans)