import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

H, W = mapint()
from collections import deque
query = [list(input()) for _ in range(H)]
dirc = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(start):
    Q = deque([start])
    checked = [[0]*W for _ in range(H)]
    checked[start[0]][start[1]] = 1
    dist = [[0]*W for _ in range(H)]
    ret = 0
    while Q:
        y, x = Q.popleft()
        ret = max(ret, dist[y][x])
        for dy, dx in dirc:
            ny, nx = y+dy, x+dx
            if ny>=H or ny<0 or nx>=W or nx<0: continue
            if query[ny][nx]=='#': continue
            if checked[ny][nx]: continue
            checked[ny][nx] = 1
            dist[ny][nx] = dist[y][x]+1
            Q.append((ny, nx))
    return ret

ans = 0
for h in range(H):
    for w in range(W):
        if query[h][w]=='#': continue
        ans = max(ans, bfs((h, w)))

print(ans)
        