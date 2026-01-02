def dfs_grid(h,w,sy, sx, maze,visited):
    cur = defaultdict(int)
    def bfs(cur):
        queue = []
        queue.insert(0, (sy, sx))
        visited[sy][sx] = True
        cur[maze[sy][sx]] += 1
        while len(queue):
            y, x = queue.pop()
            now = maze[y][x]
            for i in range(0, 4):
                nx, ny = x + [1, 0, -1, 0][i], y + [0, 1, 0, -1][i]
                if (0<= nx <w and 0<= ny <h and maze[ny][nx] != now and (not visited[ny][nx])):
                    queue.insert(0, (ny, nx))
                    visited[ny][nx] = True
                    cur[maze[ny][nx]] +=1
        return cur
    return bfs(cur)
def examC():
    H, W = LI()
    S = [SI() for _ in range(H)]
    ans = 0
    visited = [[False]*(W) for _ in range(H)]
    for i in range(H):
        for j in range(W):
            d = dfs_grid(H,W,i,j,S,visited)
            ans += d["."]*d["#"]
    print(ans)

import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

if __name__ == '__main__':
    examC()
