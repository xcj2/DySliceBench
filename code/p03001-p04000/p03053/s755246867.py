
import numpy as np
from collections import deque

def parse():
  H, W = map(int, input().split(" "))
  grid = [list(input()) for y in range(H)]
  return H, W, grid

def print_grid(grid):
  H = len(grid)
  print("grid:")
  for line in grid:
    for c in line:
      print(c, end="")
    print("")

def main():
  H, W, grid = parse()
  # print(H, W)
  # print_grid(grid)

  dark_points = [(x + 1, y + 1) for x in range(W) for y in range(H) if grid[y][x] == "#"]

  visited = [[True] * (W + 2)]
  visited += [[True] + [False for x in range(W)] + [True] for y in range(H)]
  visited.append([True for x in range(W + 2)])
  # for y in range(H + 2):
  #   print(visited[y])
  # exit(0)
  for x, y in dark_points:
    visited[y][x] = True
  
  # visited = np.zeros((H, W), int)
  # for y in range(H):
  #   for x in range(W):
  #     if grid[y][x] == ".":
  #       visited[y][x] = H * W

  # for y in range(1, H):  # ↓
  #   visited[y][:] = np.minimum(visited[y][:], visited[y - 1][:] + 1)

  # for y in range(H - 2, -1, -1):
  #   visited[y, :] = np.minimum(visited[y, :], visited[y + 1][:] + 1)

  # for x in range(1, W):
  #   visited[:, x] = np.minimum(visited[:, x], visited[:, x - 1] + 1)

  # for x in range(W - 2, -1, -1):
  #   visited[:, x] = np.minimum(visited[:, x], visited[:, x + 1] + 1)

  # print(dark_points)
  # exit(0)

  q = dark_points
  ans = 0
  while len(q) > 0:
    ans += 1
    next_q = []
    for x, y in q:
      if not visited[y - 1][x]: # 上
        visited[y - 1][x] = ans
        next_q.append((x, y - 1))
      if not visited[y + 1][x]: # 下
        visited[y + 1][x] = ans
        next_q.append((x, y + 1))
      if not visited[y][x - 1]: # 左
        visited[y][x - 1] = ans
        next_q.append((x - 1, y))
      if not visited[y][x + 1]: # 右
        visited[y][x + 1] = ans
        next_q.append((x + 1, y))
      
    # for y in range(H + 2):
    #   print(visited[y])
    # input()
    
    q = next_q

  print(ans - 1)

if __name__ == "__main__":
  main()