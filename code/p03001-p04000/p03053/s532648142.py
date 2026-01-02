def grid_bfs(h,w,start,maxD):
    INF = 10**9+7
    distance = [[INF for _ in range(w)] for _ in range(h)]
    queue = deque()
    for s in start:
        queue.append(s)
        distance[s[0]][s[1]] = 0
    while len(queue):
        y, x = queue.popleft()
        for i in range(0, 4):
            nx, ny = x + [1, 0, -1, 0][i], y + [0, 1, 0, -1][i]
            if (0 <= nx < w and 0 <= ny < h):
                if (distance[ny][nx] > distance[y][x] + 1):
                    queue.append([ny, nx])
                    distance[ny][nx] = distance[y][x] + 1
                    if maxD<distance[ny][nx]:
                        maxD = distance[ny][nx]
    return maxD
def examA():
    H, W = LI()
    A = [[1 if a == "#" else 0 for a in SI()] for _ in range(H)]
    start = []
    for i in range(H):
        for j in range(W):
            if A[i][j]==1:
                start.append([i,j])
    ans = grid_bfs(H,W,start,0)
#    print(D,V)
    print(ans)
    return

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
    examA()
