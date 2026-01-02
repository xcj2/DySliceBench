#!/usr/bin/env python3
import sys

def solve(h, w, a):
    dp = [[-1] * (h * w) for _ in range(h * w)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    def bfs(x1, y1, x2, y2):
        s = y1 * w + x1
        t = y2 * w + x2
        visited = [[False] * w for _ in range(h)]
        cur = []
        visited[y1][x1] = True
        cur.append((x1, y1))
        cnt = 1
        while True:
            nex = []
            for x, y in cur:
                for i in range(4):
                    tx = x + dx[i]
                    ty = y + dy[i]
                    if 0 <= tx < w and 0 <= ty < h and a[ty][tx] != '#' and not visited[ty][tx]:
                        visited[ty][tx] = True
                        dp[s][ty * w + tx] = cnt
                        dp[ty * w + tx][s] = cnt
                        if tx == x2 and ty == y2:
                            return cnt
                        nex.append((tx, ty))
            if len(nex) > 0:
                cur = nex
            else:
                break
            cnt += 1
        return -1

    ret = -1
    for i in range(h):
        for j in range(w):
            for i2 in range(h):
                for j2 in range(w):
                    if (i == i2 and j == j2):
                        dp[w * i + j][w * i2 + j2] = 0
                        dp[w * i2 + j2][w * i + j] = 0
                    elif a[i][j] == '.' and a[i2][j2] == '.' and dp[w * i + j][w * i2 + j2] < 0:
                        tmp = bfs(j, i, j2, i2)
                        ret = max(ret, tmp)
                        #dp[w * i + j][w * i2 + j2] = tmp
                        #dp[w * i2 + j2][w * i + j] = tmp
                        #print(i, j, i2, j2)
                        #print(tmp)
    print(ret)
    return

def main():
    h, w = map(int, input().split())
    a = []
    for i in range(h):
        a.append(input())
    solve(h, w, a)

if __name__ == '__main__':
    main()
