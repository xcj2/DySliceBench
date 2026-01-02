"""
1. スタート地点の座標を取得
2. スタート地点からbfsをして到達可能な”.”の数を数える
"""

from collections import deque

def bfs(h, w, f, s):
    count = 1
    q = deque()
    q.append(s)

    move = ((0, 1), (0, -1), (1, 0), (-1, 0))

    while q:
        i, j = q.popleft()

        for di, dj in move:
            ni , nj = i + di, j + dj
            if 0 <= ni < w and 0 <= nj < h and f[ni][nj] == ".":
                count += 1
                q.append((ni, nj))
                f[ni][nj] = "#"

    return count

def search_atmark(h, w, f):
    for i in range(h):
        for j in range(w):
            if f[i][j] == "@":
                return (i, j)

def solve(h, w, f):
    s = search_atmark(w, h, f)
    return bfs(h, w, f, s)

if __name__ == '__main__':
    while(True):
        w, h = map(int, input().split())
        if w == 0 and h == 0:
            break

        f = [list(input()) for i in range(h)]
        print(solve(w, h, f))

