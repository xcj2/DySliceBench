
from collections import deque
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


H, W = map(int, input().split())
grid = [[0]*W for _ in range(H)]

cnt = 0
for i in range(H):
    l = input()
    for j in range(W):
        grid[i][j] = l[j]
        if l[j] == '.':
            cnt += 1


# 動的計画法 dp[i][j]->grid[i][j]に行くための最短距離
dp = [[float('inf')]*W for _ in range(H)]


def check_in(x, y):
    return 0 <= x < W and 0 <= y < H


def bfs():
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    Q = deque([[0, 0]])
    dp[0][0] = 0

    while Q:
        s = Q.popleft()
        if s[0] == H-1 and s[1] == W-1:
            return
        else:
            s_x = s[1]
            s_y = s[0]
            for x, y in zip(dx, dy):
                n_x = s_x+x
                n_y = s_y+y

                if check_in(n_x, n_y):
                    if grid[n_y][n_x] != "#" and dp[n_y][n_x] == float('inf'):
                        Q.append([n_y, n_x])
                        dp[n_y][n_x] = dp[s_y][s_x]+1


def solve():
    bfs()
    min_dist = dp[H-1][W-1]
    if min_dist == float('inf'):
        return -1
    else:
        return cnt - min_dist-1


print(solve())
