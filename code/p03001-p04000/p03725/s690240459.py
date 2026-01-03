class Grid:
    def __init__(self, H, W, grid, road_wall=(".", "#")):
        self.road, self.wall = road_wall
        self.H = H
        self.W = W
        self.grid = grid
        self.parent = [[0] * self.W for _ in range(self.H)]
        self.move = [(1, 0), (-1, 0), (0, 1), (0, -1)]     # 動ける場所の候補

    def bfs(self, start=(0,0), goal=-3, time=0, save=False):
        """
        :param start: スタート地点
        :param goal: ゴール地点
        :param save: True = 前回の探索結果を保持する
        :return: （ループがあっても）最短距離。存在しなければ -1
        """
        if save:
            parent = self.parent
        else:
            parent = [[0] * self.W for _ in range(self.H)]
        p, t = start, time
        parent[p[0]][p[1]] = 1
        next_set = deque([(p, t)])
        while next_set:
            p, t = next_set.popleft()
            h, w = p
            for dh, dw in self.move:
                q = (h + dh, w + dw)
                if q[0] < 0 or q[0] >= self.H or q[1] < 0 or q[1] >= self.W:
                    continue
                if self.grid[q[0]][q[1]] == self.wall:         # 壁があったら進まない
                    continue
                if parent[q[0]][q[1]] != 0:
                    continue
                if t >= K:
                    continue
                #### (debug code) ######
                # self.debug(start, goal, q, t)
                ########################
                if q == goal:
                    return t + 1
                parent[q[0]][q[1]] = 1
                next_set.append((q, t + 1))
        return parent

    def debug(self, start, goal, p, t):
        player = p
        debug_grid = list(list(self.grid[h]) for h in range(self.H))
        if start != (None, None):
            debug_grid[start[0]][start[1]] = "S"
        if goal != -3:
            debug_grid[goal[0]][goal[1]] = "G"
        debug_grid[player[0]][player[1]] = "P"
        print("~~~~~~~~~ t = " + str(t + 1) + "  ~~~~~~~~")
        for debug_h in range(self.H):
            print("".join(str(debug_grid[debug_h][debug_w]) for debug_w in range(self.W)))


###########################################################

from collections import deque
import sys
from math import ceil
import marshal
input = sys.stdin.readline



road, wall = ".", "#"                         # (進行可能を意味する記号, 進行不可を意味する記号)

H, W, K = map(int,input().split())                # 左上は(h,w)=(0,0)、右下は(h,w)=(H-1,W-1)

grid = []
for h in range(H):
    grid.append(input().rstrip())
    for w, s in enumerate(grid[-1]):
        if s == "S":
            start = (h,w)
g = Grid(H, W, grid, (road, wall))
visit = g.bfs(start=start)
res = float("inf")
for h in range(H):
    for w in range(W):
        if visit[h][w]:
            res = min(ceil(h/K)+1,ceil(w/K)+1,ceil((H-1-h)/K)+1,ceil((W-1-w)/K)+1,res)
print(res)
