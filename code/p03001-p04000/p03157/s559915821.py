# coding:utf-8

import sys
from collections import Counter, defaultdict, deque

INF = float('inf')
MOD = 10 ** 9 + 7
dy = (0, -1, 0, 1)
dx = (1, 0, -1, 0)

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def S(): return input()


H, W = LI()
B = [[1 if s == '#' else 0 for s in S()] for _ in range(H)]


def BFS(i, j):
    white = 0
    queue = deque([(i, j)])
    visited = set()
    visited_b = set()  # 連結されている黒マス
    while queue:
        y, x = queue.pop()
        color = B[y][x]

        if color == 0 and (y, x) not in visited:
            white += 1

        if color == 1:
            visited_b.add((y, x))
        visited.add((y, x))

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if (ny, nx) in visited:
                continue

            if ny < 0 or ny >= H or nx < 0 or nx >= W:
                continue

            if B[ny][nx] == color:
                continue

            queue.append((ny, nx))

    return white, visited_b


ans = 0
visited_b = set()
for h in range(H):
    for w in range(W):
        if B[h][w] == 1 and (h, w) not in visited_b:
            tmp, v = BFS(h, w)
            ans += tmp * len(v)
            visited_b |= v

print(ans)
