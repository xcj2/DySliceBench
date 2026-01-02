
from collections import deque
from copy import deepcopy

def parse():
  H, W = map(int, input().split(" "))
  grid = []
  grid.append(["#" for x in range(W + 2)])
  for y in range(H):
    grid.append(list("#" + input() + "#"))
  grid.append(["#" for x in range(W + 2)])
  return H, W, grid

def print_grid(grid):
  H = len(grid)
  W = len(grid[0])
  for y in range(H):
    for x in range(W):
      print(grid[y][x], end="")
    print("")
  print("")

def print_visited(visited):
  H = len(visited)
  W = len(visited[0])
  for y in range(H):
    for x in range(W):
      if visited[y][x]:
        print(1, end="")
      else:
        print(0, end="")
    print("")
  print("")

def print_grid_with_paths(grid, paths):
  H = len(grid)
  W = len(grid[0])
  for y in range(H):
    for x in range(W):
      if (x, y) in paths:
        print("*", end="")
      else:
        print(grid[y][x], end="")
    print("")
  print("")

def main():
  H, W, grid = parse()

  visited = [[False for x in range(W + 2)] for y in range(H + 2)]
  for y in range(H + 2):
    for x in range(W + 2):
      if x == 0 or x == W + 1 or y == 0 or y == H + 1:
        visited[y][x] = True
  visited[0][0] = True

  # print_grid(grid)
  # print_visited(visited)

  vecs = [(0, -1), (0, 1), (-1, 0), (1, 0)]

  # 幅優先探索で最短経路を求める
  q = deque([(1, 1, [])])
  while len(q) > 0:
    x, y, paths = q.popleft()
    paths.append((x, y))
    # print_grid_with_paths(grid, paths)
    # input()
    
    # 終了条件
    if y == H and x == W:
      # print(paths)
      ans = 0
      for y in range(H + 2):
        for x in range(W + 2):
          # 経路は除外
          if (x, y) in paths:
            continue

          if grid[y][x] == ".":
            ans += 1

      # 最短経路周辺に"#"を置く数をカウント
      # prev_x, prev_y = paths[0]
      # cur_x, cur_y = paths[1]
      # for next_x, next_y in paths[2:]:
      #   for vec in vecs:
      #     adj_x = cur_x + vec[0]
      #     adj_y = cur_y + vec[1]

      #     # 経路上のマスの色は変えない
      #     if adj_x == prev_x and adj_y == prev_y:
      #       continue
      #     if adj_x == next_x and adj_y == next_y:
      #       continue
          
      #     # マスの色を変える
      #     if grid[adj_y][adj_x] == ".":
      #       grid[adj_y][adj_x] = "#"
      #       ans += 1
      #   prev_x, prev_y = cur_x, cur_y
      #   cur_x, cur_y = next_x, next_y
      #   # print_grid(grid)
      #   # input()
      print(ans)
      exit(0)

    for vec in vecs:
      next_x = x + vec[0]
      next_y = y + vec[1]
      if grid[next_y][next_x] == "#":
        continue

      if not visited[next_y][next_x]:
        visited[next_y][next_x] = True
        q.append((next_x, next_y, deepcopy(paths)))

  print(-1)

if __name__ == "__main__":
  main()