import sys
from collections import deque

sys.setrecursionlimit(10**5)

def solve():
    while 1:
        w, h = map(int, sys.stdin.readline().split())

        if w == h == 0:
            return

        room = [[int(j) for j in sys.stdin.readline().split()] for i in range(h)]

        cnt = 0

        for i in range(h):
            for j in range(w):
                if room[i][j]:
                    cnt += 1
                    bfs(w, h, room, i, j)

        print(cnt)

dx = (1, 0, -1, 0, 1, 1, -1, -1)
dy = (0, 1, 0, -1, 1, -1, 1, -1)

def bfs(w, h, room, i, j):
    room[i][j] = 0
    q = deque([(i, j)])

    while q:
        ci, cj = q.popleft()

        for k in range(len(dx)):
            ni = ci + dy[k]
            nj = cj + dx[k]

            if 0 <= ni < h and 0 <= nj < w and room[ni][nj]:
                room[ni][nj] = 0
                q.append((ni, nj))

    return

def dfs(w, h, room, i, j):
    if i < 0 or i >= h or j < 0 or j >= w or (not room[i][j]):
        return

    room[i][j] = 0

    dfs(w, h, room, i + 1, j)
    dfs(w, h, room, i - 1, j)
    dfs(w, h, room, i, j + 1)
    dfs(w, h, room, i, j - 1)
    dfs(w, h, room, i + 1, j + 1)
    dfs(w, h, room, i + 1, j - 1)
    dfs(w, h, room, i - 1, j + 1)
    dfs(w, h, room, i - 1, j - 1)

if __name__ == '__main__':
    solve()