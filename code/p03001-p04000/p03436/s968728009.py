class Grid:
    def __init__(self, H, W, grid, road_wall=(".", "#"), destroy=False):
        self.road, self.wall = road_wall
        self.H = H
        self.W = W
        self.destroy = destroy
        self.grid = grid
        self.parent = [[(-1,-1)] * self.W for _ in range(self.H)]
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
            parent = [[-1] * self.W for _ in range(self.H)]
        p, t = start, time
        parent[p[0]][p[1]] = -2
        next_set = deque([(p, t)])
        while next_set:
            p, t = next_set.popleft()
            h0, w0 = p
            for dh, dw in self.move:
                h, w = (h0 + dh, w0 + dw)
                if h < 0 or h >= self.H or w < 0 or w >= self.W:
                    continue
                if self.grid[h][w] == self.wall:         # 壁があったら進まない
                    continue
                if parent[h][w] != -1:
                    continue
                #### (debug code) ######
                # self.debug(start, goal, (h,w), t)
                ########################
                if (h,w) == goal:
                    return t + 1
                parent[h][w] = p
                next_set.append(((h, w), t + 1))
        return -1

    def connection_counter(self):
        """
        :return: 連結成分の個数。有効グラフではあまり意味がない。
        """
        cnt = 0
        self.parent = [[-1] * self.W for _ in range(self.H)]
        for h in range(self.H):
            for w in range(self.W):
                if self.parent[h][w] == -1:
                    cnt += 1
                    self.bfs(start=(h,w), save=True)
        return cnt

    def distance_list(self, start=(0,0), save=False):
        """
        :param start: スタート地点
        :return: スタート地点から各点への距離のリスト
        """
        dist = [[-1] * self.W for _ in range(self.H)]
        if save:
            parent = self.parent
        else:
            parent = [[-1] * self.W for _ in range(self.H)]
        p, t = start, 0
        parent[p[0]][p[1]] = -2
        dist[p[0]][p[1]] = 0
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
                if parent[q[0]][q[1]] != -1:
                    continue
                dist[q[0]][q[1]] = t + 1
                parent[q[0]][q[1]] = p
                next_set.append((q, t + 1))
        return dist

    def most_distant_point(self, start=(0, 0), save=False):
        """
        :param start:
        :return: start 地点から最も遠い点を ((h,w), 距離) として出力
        """
        res = (start, 0)
        temp = 0
        dist = self.distance_list(start, save=save)
        for h in range(self.H):
            for w in range(self.W):
                if dist[h][w] > temp:
                    temp = dist[h][w]
                    res = ((h, w), temp)
        return res

    def diameter(self, start=(0,0), save=False):
        """
        :return:　木の直系（最も離れた二頂点間の距離）を返す
        """
        p = self.most_distant_point(start, save=False)
        res = self.most_distant_point(start=p[0], save=save)
        return res[1]

    def diameter2(self):
        """
        :return:　連結ではない時に、最大の直系を返す
        """
        res = 0
        for h in range(self.H):
            for w in range(self.W):
                if self.grid[h][w] == self.road and self.parent[h][w] == -1:
                    temp = self.diameter(start=(h, w), save=False)
                    if temp > res:
                        res = temp
        return res

    def dfs(self, start=(0, 0), goal=-3, time=0, save=False):
        """
        :param start: スタート地点
        :param goal: ゴール地点
        :param save: True = 前回の探索結果を保持する
        :return: ゴール地点までの距離。存在しなければ -1。ループがある時は最短距離とは限らないため注意。
        """

        if save:
            parent = self.parent
        else:
            parent = [[-1] * self.W for _ in range(self.H)]
        move2 = [[marshal.loads(marshal.dumps(self.move)) for _ in range(self.W)] for _ in range(self.H)]

        p, t = start, time
        parent[p[0]][p[1]] = -2
        while True:
            if move2[p[0]][p[1]]:
                h, w = p
                dh, dw = move2[p[0]][p[1]].pop()
                q = (h + dh, w + dw)
                if q[0] < 0 or q[0] >= self.H or q[1] < 0 or q[1] >= self.W:
                    continue
                if self.grid[q[0]][q[1]] == self.wall:         # 壁があったら進まない
                    continue
                if q == parent[p[0]][p[1]]:
                    """ 逆流した時の処理 """
                    """"""""""""""""""""
                    continue
                if parent[q[0]][q[1]] != -1:
                    """ サイクルで同一点を訪れた時の処理 """
                    """"""""""""""""""""
                    continue
                #### (debug code) ######
                # self.debug(start, goal, q, t)
                # self.show_visited(start, goal, q, t, parent)
                ########################
                if q == goal:
                    """ ゴール時の処理"""
                    """"""""""""""""""""
                    return t + 1
                """ p から q への引継ぎ"""
                """"""""""""""""""""
                parent[q[0]][q[1]] = p
                p, t = q, t + 1
            else:
                if p == start and t == time:
                    break
                p_temp = p
                p, t = parent[p[0]][p[1]], t-1
                """ p から進める点がもう無い時の点 p における処理 """
                # parent[p_temp[0]][p_temp[1]] = -1
                # move2[p_temp[0]][p_temp[1]].extend(marshal.loads(marshal.dumps(self.move)))
                """"""""""""""""""""
                """ 点 p から親ノードに戻ってきた時の親ノードにおける処理 """
                """"""""""""""""""""
        return -1

    def dfs2(self, start=(0, 0), goal=-3, time=0):
        visited = [[-1] * self.W for _ in range(self.H)]
        p, t = start, time
        res = 0
        def rec(p, past_p, t, visited, res):
            h, w = p
            visited[p[0]][p[1]] = 1
            for dh, dw in self.move:
                q = (h + dh, w + dw)
                if q[0] < 0 or q[0] >= self.H or q[1] < 0 or q[1] >= self.W:
                    continue
                if grid[q[0]][q[1]] == self.wall:
                    continue
                if q == past_p:
                    """ 逆流した時の処理 """
                    """"""""""""""""""""
                    continue
                if visited[q[0]][q[1]] == 1:
                    """ サイクルで同一点を訪れた時の処理 """
                    """"""""""""""""""""
                    continue
                """ (debug code) """
                # self.debug(start, goal, q, t)
                # self.show_visited(start, goal, q, t, visited)
                """"""""""""""""""""
                if q == goal:
                    """ ゴール時の処理"""
                    """"""""""""""""""""
                    return t+1
                res = max2(rec(q, p, t + 1, visited, res), t + 1)
            """ 帰り際の処置（壊した道を元に戻す等)"""
            # visited[p[0]][p[1]] = -1
            """"""""""""""""""""
            return res
        return rec(p, -1, t, visited, res)

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

    def show_visited(self, start, goal, p, t, parent):
        player = p
        debug_grid = list(list(self.grid[h]) for h in range(self.H))
        for h in range(H):
            for w in range(W):
                if parent[h][w] != -1:
                    debug_grid[h][w] = "V"
        if start != (None, None):
            debug_grid[start[0]][start[1]] = "S"
        if goal != -3:
            debug_grid[goal[0]][goal[1]] = "G"
        debug_grid[player[0]][player[1]] = "P"
        print("~~~~~~~~~ t = " + str(t + 1) + "  ~~~~~~~~")
        for debug_h in range(self.H):
            print("".join(str(debug_grid[debug_h][debug_w]) for debug_w in range(self.W)))

############################################################################################

from collections import deque
import sys
import marshal
input = sys.stdin.readline



road, wall = ".", "#"                         # (進行可能を意味する記号, 進行不可を意味する記号)

H, W = map(int,input().split())                # 左上は(h,w)=(0,0)、右下は(h,w)=(H-1,W-1)

grid = []
cnt = 0
for h in range(H):
    grid.append(input().rstrip())
    cnt += grid[-1].count(".")
start = (0,0)
goal = (H-1, W-1)

g = Grid(H, W, grid, (road, wall), destroy=False)
res = g.bfs(start, goal)
if res == -1:
    print(-1)
else:
    print(cnt - res - 1)
