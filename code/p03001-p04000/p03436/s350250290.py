#!/usr/bin/env python3

from collections import deque

H, W = map(int, input().split())

field = []
for _ in range(H):
    line = list(input())
    field.append(line)
# print(H, W, field)


def is_valid(i, j):
    cond_i = 0 <= i <= H - 1
    cond_j = 0 <= j <= W - 1
    return cond_i and cond_j


def is_reachable(i, j, ):
    if is_valid(i, j):
        if field[i][j] == '.':
            return True
    return False


def adj(i, j):
    up, down = [i - 1, j], [i + 1, j]
    left, right = [i, j - 1], [i, j + 1]
    res = []
    for i_adj, j_adj in up, down, left, right:
        if is_reachable(i_adj, j_adj):
            res.append([i_adj, j_adj])
    return res


def bfs(que, dist):
    while len(que) > 0:
        i, j = que.popleft()
        # print(f"i, j: {i}, {j}")
        for i_adj, j_adj in adj(i, j):
            # print(f"i_adj, j_adj: {i_adj}, {j_adj}")
            if dist[(i_adj, j_adj)] == -1:
                que.append([i_adj, j_adj])
                dist[(i_adj, j_adj)] = dist[(i, j)] + 1


que = deque()
keys = [(i, j) for i in range(H) for j in range(W)]
values = [-1 for _ in range(H * W)]
dist = dict(zip(keys, values))
# print(dist)

n_black = 0
for i in range(H):
    for j in range(W):
        if field[i][j] == '#':
            n_black += 1

que.append([0, 0])
dist[(0, 0)] = 0
bfs(que, dist)

if dist[(H - 1, W - 1)] == -1:
    print(-1)
else:
    steps_min = dist[(H - 1, W - 1)] + 1
    n_white = W * H - n_black
    ans = n_white - steps_min
    print(ans)
