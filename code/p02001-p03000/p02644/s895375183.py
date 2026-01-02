import sys
import math
from collections import defaultdict, deque
def r():
    return int(input())
def rm():
    return map(int,input().split())
def rl():
    return list(map(int,input().split()))

def bfs(maze, visited, sy, sx, gy, gx):
    queue = deque([[sy, sx]])
    visited[sy][sx] = 0
    while queue:
        y, x = queue.popleft()
        if [y, x] == [gy, gx]:
            return visited[y][x]
        for j, k in ([1, 0], [-1, 0], [0, 1], [0, -1]):
          p = 0
          l = 1
          while p == 0:
              new_y, new_x = y + j * l, x + k * l
              if (0 <= new_y < H) and (0 <= new_x < W):
                if maze[new_y][new_x] == "@":
                  p = 1
                elif visited[new_y][new_x] == -1:
                  visited[new_y][new_x] = visited[y][x] + 1
                  queue.append([new_y, new_x])
                elif visited[new_y][new_x] < visited[y][x] + 1:
                  p = 1
              else:
                p = 1
              l += 1
              if l == K + 1:
                p = 1

H, W, K = rm()
x1, y1, x2, y2 = rm()
x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
C = [0] * H
for i in range(H):
  C[i] = str(input())
visited = [[-1] * W for i in range(H)]
bfs(C, visited, x1, y1, x2, y2)
print(visited[x2][y2])