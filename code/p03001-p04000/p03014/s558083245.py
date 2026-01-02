import sys
stdin = sys.stdin

sys.setrecursionlimit(10 ** 7)

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x) - 1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

h, w = li()
grid = [lc() for _ in range(h)]

# 左側の照らせるマス
left = [[0]*w for _ in range(h)]
for row in range(h):
    cur = 0
    for col in range(w-1, -1, -1):
        if grid[row][col] == ".":
            cur += 1
            left[row][col] = cur
        else:
            cur = 0

# 右側の照らせるマス
right = [[0]*w for _ in range(h)]
for row in range(h):
    cur = 0
    for col in range(w):
        if grid[row][col] == ".":
            cur += 1
            right[row][col] = cur
        else:
            cur = 0

# 上側の照らせるマス
up = [[0]*w for _ in range(h)]
for col in range(w):
    cur = 0
    for row in range(h-1, -1, -1):
        if grid[row][col] == ".":
            cur += 1
            up[row][col] = cur
        else:
            cur = 0

# 下側の照らせるマス
down = [[0]*w for _ in range(h)]
for col in range(w):
    cur = 0
    for row in range(h):
        if grid[row][col] == ".":
            cur += 1
            down[row][col] = cur
        else:
            cur = 0

# 最大値
ans = 0
for row in range(h):
    for col in range(w):
        ans = max(ans, left[row][col] + right[row][col] + up[row][col] + down[row][col])

print(ans-3)
