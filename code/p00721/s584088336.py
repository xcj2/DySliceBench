import sys
import math
import bisect
import heapq
import copy
sys.setrecursionlimit(1000000)
from collections import deque
from itertools import permutations

dy = [-1,0,1,0]
dx = [0,1,0,-1]

def main():
    m,n = 0,0
    grid = []
    inf = 1000000007

    def in_the_grid(h,w):
        return 0<=h and h<n  and 0<=w and w<m

    def bfs(i,j):
        dq = deque()
        res = [[inf]*m for _ in range(n)]
        dq.append([i,j,0])
        res[i][j] = 0
        while dq:
            h,w,c = dq.popleft()
            for k in range(4):
                n_h = h+dy[k]
                n_w = w+dx[k]
                if not in_the_grid(n_h,n_w):continue
                if grid[n_h][n_w] == 'x':continue
                if res[n_h][n_w]!=inf:continue
                res[n_h][n_w] = c+1
                dq.append([n_h,n_w,c+1])
        return res

    while True:
        m,n = map(int,input().split())
        if m == 0:break
        grid = []
        dis = []
        ver = []
        for _ in range(n):
            grid.append(input())
        for i in range(n):
            for j in range(m):
                if grid[i][j]=='o':
                    ver.append([i,j])
                    dis.append(bfs(i,j))
        for i in range(n):
            for j in range(m):
                if grid[i][j]=='*':
                    ver.append([i,j])
                    dis.append(bfs(i,j))

        v = len(dis)
        d = [[] for _ in range(v)]
        for i in range(v):
            for j,k in ver:
                d[i].append(dis[i][j][k])

        dp = [[inf]*v for _ in range(1<<v)]
        dp[1][0] = 0
        for bits in range(1<<v):
            for i in range(v):
                if dp[bits][i] == inf:continue
                for j in range(v):
                    if bits&(1<<j):continue
                    dp[bits|(1<<j)][j] = min(dp[bits|(1<<j)][j],
                                             dp[bits][i]+d[i][j])

        ans = inf
        for i in range(1,v):ans = min(ans,dp[(1<<v)-1][i])
        print (ans if ans!=inf else -1)


if __name__ == '__main__':
    main()


