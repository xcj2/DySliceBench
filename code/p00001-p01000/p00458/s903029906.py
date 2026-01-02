# -*- coding: utf-8 -*-
"""

"""
import sys
from sys import stdin
from collections import deque
input = stdin.readline


def bfs(H, W, maze, sx, sy):
    max_ans = 1
    # 上下左右に移動する場合の座標の変化量
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    path = [(sx, sy)]           #  切り取りに含める切手の座標 (まずは探索開始地点のみからスタート)
    Q = deque()
    Q.append((sx, sy, path))
    while Q:
        cx, cy, path = Q.popleft()        #  現在地の座標と探索状況
        for i in range(len(dx)):
            nx = cx + dx[i]
            ny = cy + dy[i]
            #  移動先まで通行可能 かつ 既に探索済でなければ、その先でも探索を続ける
            if 0 <= nx < W and 0 <= ny < H and not (nx, ny) in path and maze[ny][nx] == 1:
                t = path[:]
                t.append((nx, ny))
                ans = len(t)
                if ans > max_ans:
                    max_ans = ans
                Q.append((nx, ny, t[:]))
    return max_ans


def solve(H, W, maze):
    # 全てのマスを起点にして、条件を満たす切り取り方をチェックする
    ans = 0
    for y in range(H):
        for x in range(W):
            if maze[y][x] == 1:
                t = bfs(H, W, maze, x, y) #  座標x, yを起点にした解の一覧
                ans = max(ans, t)
    return ans


def main(args):
    while True:
        W = int(input())
        H = int(input())
        if W == 0 and H == 0:
            break
        maze = []
        for _ in range(H):
            maze.append([int(x) for x in input().split()])
        ans = solve(H, W, maze)
        print(ans)

if __name__ == '__main__':
    main(sys.argv[1:])


