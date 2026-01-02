import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**5) 
 
def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

from collections import deque

def bfs(grid):
    h = len(grid)
    w = len(grid[0])
    
    dist = [[float('inf')]*w for _ in range(h)]
    
    que = deque([])
    que.append(((0,0), 1))
    dist[0][0] = 0
    
    drs = [-1,0,1,0]
    dcs = [0,-1,0,1]
    
    while que:
        (rcur, ccur), cost = que.popleft()
        if rcur == h-1 and ccur == w-1:
            return dist[h-1][w-1]
    
        for dr, dc in zip(drs, dcs):
            if not (0 <= rcur+dr < h and 0 <= ccur+dc < w):
                continue
            
            elif grid[rcur+dr][ccur+dc] == '#':
                continue
            
            elif dist[rcur+dr][ccur+dc] != float('inf'):
                continue
            
            dist[rcur+dr][ccur+dc] = cost + 1
            que.append(((rcur+dr, ccur+dc), cost+1))
            
    return -1
            

h,w = li()
grid = [lc() for _ in range(h)]

white = 0
for row in grid:
    for col in row:
        if col == '.':
            white += 1

route = bfs(grid)
print(-1 if route == -1 else white - route)