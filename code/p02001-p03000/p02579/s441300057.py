#!/usr/bin/env python3
import sys
from collections import deque
from math import inf


def input(): return sys.stdin.readline().strip()


def bfs(maze, Ch, Cw, Dh, Dw, H, W):
    visited = [[inf] * W for i in range(H)]
    queue = deque([[Ch, Cw]])
    visited[Ch][Cw] = 0

    dy_dx0 = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    dy_dx1 = [[2, 2], [2, 1], [2, 0], [2, -1], [2, -2], [1, 2], [1, 1], [1, -1], [1, -2], [0, 2],
              [0, -2], [-1, 2], [-1, 1], [-1, -1], [-1, -2], [-2, 2], [-2, 1], [-2, 0], [-2, -1], [-2, -2]]

    while queue:
        y, x = queue.popleft()
        if [y, x] == [Dh, Dw]:
            break
        for j, k in dy_dx0:
            new_y, new_x = y + j, x + k
            if 0 <= new_y < H and 0 <= new_x < W and maze[new_y][new_x] == "." and visited[y][x] < visited[new_y][new_x]:
                visited[new_y][new_x] = visited[y][x]
                queue.appendleft([new_y, new_x])
        for j, k in dy_dx1:
            new_y, new_x = y + j, x + k
            if 0 <= new_y < H and 0 <= new_x < W and maze[new_y][new_x] == "." and visited[new_y][new_x] == inf:
                visited[new_y][new_x] = visited[y][x] + 1
                queue.append([new_y, new_x])
    return visited[Dh][Dw]


def main():
    H, W = map(int, input().split())
    Ch, Cw = map(int, input().split())
    Dh, Dw = map(int, input().split())
    maze = [input() for i in range(H)]

    dist = bfs(maze, Ch - 1, Cw - 1, Dh - 1, Dw - 1, H, W)

    print(dist if dist != inf else -1)


if __name__ == "__main__":
    main()
