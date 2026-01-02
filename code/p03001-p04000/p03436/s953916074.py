# -*- coding: utf-8 -*-
"""
https://abc088.contest.atcoder.jp/tasks/abc088_d

"""
import sys
from sys import stdin
from collections import deque
input = stdin.readline


def bfs(grid, H, W):
    # 上下左右に移動する場合の座標の変化量
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    gx, gy = W-1, H-1

    # 地図のサイズ(移動によってはみ出さないかのチェックに使用)
    d = [[float('inf')] * W for _ in range(H)] #  スタート地点からの距離をINFで初期化
    # 迷路を歩いて、スタート地点からゴール地点までの距離を求める
    Q = deque()
    Q.append((0, 0))
    d[0][0] = 0               #  スタート地点のコストは0
    while Q:
        cx, cy = Q.popleft()        #  現在地の座標
        if cx == gx and cy == gy:
            return d[gy][gx]
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            # 移動先が 地図からはみ出しておらず and 壁になっておらず and 既に探索済でない 場合
            if (0 <= nx < W) and (0 <= ny < H) and grid[ny][nx] != '#' and d[ny][nx] == float('inf'):
                Q.append((nx, ny))
                d[ny][nx] = d[cy][cx] + 1
    return -1



def solve(grid, H, W):
    step = bfs(grid, H, W)
    if step < 0:
        return -1

    orig_black = 0
    for row in grid:
        orig_black += row.count('#')
    return H*W - orig_black - step -1


def main(args):
    grid = []
    H, W = map(int, input().split())
    for _ in range(H):
        grid.append(list(input().strip()))
    ans = solve(grid, H, W)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
    