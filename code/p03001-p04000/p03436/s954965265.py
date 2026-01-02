from sys import stdin


def fetch_one_line():
    return stdin.readline().rstrip()


def fetch_int_input():
    return [int(s) for s in fetch_one_line().split()]


def fetch_inputs(times):
    return [fetch_one_line() for _ in range(times)]


def fetch_int_inputs(times):
    return [[int(s) for s in fetch_one_line()] for _ in range(times)]

import sys
from collections import deque

moves = ((1, 0), (0, 1), (-1, 0), (0, -1))
H, W = fetch_int_input()
maze = [list(fetch_one_line()) for _ in range(H)]
X, Y = 0, 1
STARTS = (0, 0)
GOALS = (H - 1, W - 1)


def count_wall(maze, wall="#"):
    wall_num = 0
    for one_line in maze:
        wall_num += "".join(one_line).count(wall)
    return wall_num

def bfs():
    que = deque()
    d = [[sys.maxsize for _ in range(W)] for _ in range(H)]
    que.append(STARTS)
    d[STARTS[X]][STARTS[Y]] = 0

    while que:
        now_pos = que.popleft()
        if now_pos == GOALS:
            break
        for move in moves:
            np = (now_pos[X] + move[X], now_pos[Y] + move[Y])
            if np[X] >= 0 and np[Y] >= 0 and np[X] < H and np[Y] < W and maze[np[X]][np[Y]] == '.' and d[np[X]][np[Y]] == sys.maxsize:
                que.append(np)
                d[np[X]][np[Y]] = d[now_pos[X]][now_pos[Y]] + 1

    return d[GOALS[X]][GOALS[Y]]

min_distance = bfs()
if min_distance == sys.maxsize:
    changable_num = -1
else:
    wall_num = count_wall(maze, "#")
    changable_num = H * W - 2 - (min_distance - 1) - wall_num
print(changable_num)
