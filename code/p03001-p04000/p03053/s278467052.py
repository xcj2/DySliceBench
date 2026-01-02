
import numpy as np

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

  # visited = [[W * H if grid[y][x] == "." else 0 for x in range(W)] for y in range(H)]
  visited = np.zeros((H, W), int)
  for y in range(H):
    # visited.append([])
    for x in range(W):
      if grid[y][x] == ".":
        visited[y][x] = H * W

  for y in range(1, H):  # ↓
    # 要素ごとの処理
    # print(visited)
    visited[y][:] = np.minimum(visited[y][:], visited[y - 1][:] + 1)
    # print(visited)
    # input()
    # print(visited[y])
    # exit(0)

  for y in range(H - 2, -1, -1):
    visited[y, :] = np.minimum(visited[y, :], visited[y + 1][:] + 1)

  for x in range(1, W):
    visited[:, x] = np.minimum(visited[:, x], visited[:, x - 1] + 1)

  for x in range(W - 2, -1, -1):
    visited[:, x] = np.minimum(visited[:, x], visited[:, x + 1] + 1)

  # print(visited)
  # exit(0)

  # max_len = 0
  # for y in range(H):
  #   max_val = max(visited[y])
  #   max_len = max_len if max_len > max_val else max_val
  # print(max_len)
  print(np.max(visited))

if __name__ == "__main__":
  main()