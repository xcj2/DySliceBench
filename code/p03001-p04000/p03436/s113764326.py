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

def bfs(grid: list):
    h = len(grid)
    w = len(grid[0])
    
    dhs = [0, 1, 0, -1]
    dws = [1, 0, -1, 0]
    
    que = deque([(1,(0,0))])
    grid[0][0] = "1"
    
    while que:
        cost, (hcur, wcur) = que.popleft()
    
        for dh, dw in zip(dhs, dws):
            if 0 <= hcur+dh < h and 0 <= wcur+dw < w and grid[hcur+dh][wcur+dw] == ".":
                nex_cost = cost + 1
                grid[hcur+dh][wcur+dw] = str(nex_cost)
                que.append((nex_cost, (hcur+dh, wcur+dw)))
    

h,w = li()

grid = []
for _ in range(h):
    grid.append(lc())

whites = 0
for row in grid:
    whites += row.count(".")

bfs(grid)

if grid[-1][-1] == "#" or grid[-1][-1] == ".":
    print(-1)

else:
    print(whites - int(grid[-1][-1]))