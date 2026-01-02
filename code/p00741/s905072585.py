# -*- coding: utf-8 -*-
"""
How Many Islands?
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1160&lang=jp

"""
import sys
from sys import stdin
from collections import deque
input = stdin.readline


def bfs(data, sx, sy, w, h):
    dy = [-1, 1, 0, 0, -1, -1, 1, 1]
    dx = [0, 0, -1, 1, -1, 1, -1, 1]
    Q = deque()
    Q.append((sx, sy))
    data[sy][sx] = '-'
    while Q:
        cx, cy = Q.popleft()        #  現在地の座標
        for i in range(8):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if (not 0 <= nx < w) or (not 0 <= ny < h):
                continue
            elif data[ny][nx] == '1':
                Q.append((nx, ny))
                data[ny][nx] = '-'


def solve(field, w, h):
    ans = 0
    for y in range(h):
        for x in range(w):
            if field[y][x] == '1':
                bfs(field, x, y, w , h)
                ans += 1
    return ans


def main(args):
    while True:
        w, h = map(int, input().split())
        if w == 0 and h == 0:
            break
        field = []
        for _ in range(h):
            field.append([x for x in input().split()])
        ans = solve(field, w, h)
        print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])

