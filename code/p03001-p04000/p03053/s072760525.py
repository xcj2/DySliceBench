import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

H, W = mapint()
As = [list(input()) for _ in range(H)]
dist = [[10**18]*W for _ in range(H)]
dirc = ((-1, 0), (1, 0), (0, -1), (0, 1))

from collections import deque
def bfs(start_lis):
    Q = deque()
    for sy, sx in start_lis:
        dist[sy][sx] = 0
        Q.append((sy, sx))
    while Q:
        y, x = Q.popleft()
        for dy, dx in dirc:
            ny, nx = y+dy, x+dx
            if ny>=H or ny<0 or nx>=W or nx<0:
                continue
            if dist[ny][nx]>dist[y][x]+1:
                dist[ny][nx] = dist[y][x]+1
                Q.append((ny, nx))

start_lis = []
for h in range(H):
    for w in range(W):
        if As[h][w]=='#':
            start_lis.append((h, w))
bfs(start_lis)
ans = 0
for h in range(H):
    for w in range(W):
        ans = max(ans, dist[h][w])
print(ans)