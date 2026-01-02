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
    global count 
    
    d = [[-1] * w for i in range(h)]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    que = deque([])
    que.append((sx, sy))#スタート座標の記録
    d[sx][sy] = 0#スタートからスタートへの最短距離は0

    while que:#中身がなくなるまで
        p = que.popleft()
        if p[0] == h-1 and p[1] == w-1:#ゴールなら終わり
            break
        for m in range(4):#現在地から4方向の移動を考える
            nx = p[0] + dx[m]
            ny = p[1] + dy[m]

            if 0 <= nx < h and 0 <= ny < w:
              if maze[nx][ny] != "#" and d[nx][ny] == -1:
                que.append((nx, ny))#↑範囲内である＆壁でない＆まだ通ってない
                d[nx][ny] = d[p[0]][p[1]] + 1

    if d[h-1][w-1] == -1:
      return -1
    else:
      for i in range(h):
        count += maze[i].count('.')
      count -= 2#スタートとゴールの分引いた
      return count - d[h-1][w-1] + 1
  
  

h,w = MAP()
maze = [list(input()) for i in range(h)]
count = 0

print(bfs(0,0))
