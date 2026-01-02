from collections import deque,defaultdict
import sys
def bfs(s,g,n):
    bfs_map = [-1]*n
    bfs_map[s] = 0
    q = deque([s])
    while q:
        x = q.popleft()
        for y in v[x]:
            if c[x][y] > 0 and bfs_map[y] < 0:
                bfs_map[y] = bfs_map[x]+1
                q.append(y)
    return bfs_map

def update(s,g,bfs_map):
    f = float("inf")
    p = [[None]*2 for i in range(bfs_map[g])]
    y = g
    for i in range(bfs_map[g])[::-1]:
        p[i][1] = y
        for x in v[y]:
            if c[x][y] > 0 and bfs_map[x] == i:
                if c[x][y] < f:
                    f = c[x][y]
                y = x
                p[i][0] = x
                break
        else:
            return 0

    for x,y in p:
        c[x][y] -= f
        c[y][x] += f
    return f

def dinic(s,g,n):
    f = 0
    while 1:
        bfs_map = bfs(s,g,n)
        if bfs_map[g] < 0:
            return f
        cap = update(s,g,bfs_map)
        while cap > 0:
            f += cap
            cap = update(s,g,bfs_map)
if __name__ == "__main__":
    n,e = map(int, sys.stdin.readline()[:-1].split())
    v = [[] for i in range(n)]
    c = [[0]*n for i in range(n)]
    for i in range(e):
        a,b,w = map(int,sys.stdin.readline()[:-1].split())
        v[a].append(b)
        v[b].append(a)
        c[a][b] = w
    print(dinic(0,n-1,n))

