import heapq
import sys

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(s) for s in input().split(" ")]

def log(*args):
    print("DEBUG:", *args, file=sys.stderr)

h,w = get_nums_l()
grid = [ input() for _ in range(h) ]
dp = [ [99999999999999999999] * w for _ in range(h)]

def bfs(cost, x, y):
    # log(cost, y, x)
    if dp[y][x] <= cost:
        return

    dp[y][x] = cost

    if x < w-1:
        if grid[y][x] == "." and grid[y][x+1] == "#":
            heapq.heappush(heap, (cost+1, x+1, y))
        else:
            heapq.heappush(heap, (cost, x+1, y))

    if y < h-1:
        if grid[y][x] =="." and grid[y+1][x] == "#":
            heapq.heappush(heap, (cost+1, x, y+1))
        else:
            heapq.heappush(heap, (cost, x, y+1))

heap = []

if grid[0][0] == ".":
    heapq.heappush(heap, (0,0,0))
else:
    heapq.heappush(heap, (1,0,0))

while heap:
    cost, x, y = heapq.heappop(heap)
    bfs(cost, x, y)

print(dp[h-1][w-1])
