import math
from functools import reduce
from collections import deque
import sys
sys.setrecursionlimit(10**7)
import copy

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(s) for s in input().split(" ")]

# 改行区切りの入力をn行読み込んで数値リストにして返します。
def get_nums_n(n):
    return [ int(input()) for _ in range(n)]

# 改行またはスペース区切りの入力をすべて読み込んでイテレータを返します。
def get_all_int():
    return map(int, open(0).read().split())

def log(*args):
    print("DEBUG:", *args, file=sys.stderr)

def neighbors4(x, y):
  dxy = (0, 1, 0, -1, 0 )
  for i in range(4):
    yield(x + dxy[i], y + dxy[i+1])

h,w = get_nums_l()

grid_s = [ input() for _ in range(h) ]
grid = [ [-1] * (w+2) for _ in range(h+2) ]

log(grid_s)

def init_grid():
    for y in range(1,h+1):
        for x in range(1, w+1):
            if grid_s[y-1][x-1] == ".":
                grid[y][x] = 999999999999999999

ans = 0
for y in range(1,h+1):
    for x in range(1, w+1):
        if grid_s[y-1][x-1] == ".":
            init_grid()
            grid[y][x] = 0

            que = deque()
            que.append((x, y, 1))

            max_ = 0
            while que:
                x,y,score = que.popleft()

                for nx,ny in neighbors4(x,y):
                    if grid[ny][nx] != -1 and grid[ny][nx] > score:
                        grid[ny][nx] = score
                        max_ = max(max_, score)
                        que.append((nx, ny, score+1))
            ans = max(ans, max_)

print(ans)