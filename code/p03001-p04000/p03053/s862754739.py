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

h,w = li()
a = [list(lc()) for _ in range(h)]

que = deque()

dist = [[-1]*w for _ in range(h)]

for i, ai in enumerate(a):
    for j, aij in enumerate(ai):
        if aij == "#":
            que.append((0, (i, j)))
            dist[i][j] = 0
        
drs = [0,1,0,-1]
dcs = [1,0,-1,0]

while que:
    cur, (r,c) = que.popleft()
    dist[r][c] = cur
    
    for dr, dc in zip(drs, dcs):
        if 0 <= r+dr < h and 0 <= c+dc < w:
            if dist[r+dr][c+dc] == -1:
                dist[r+dr][c+dc] = cur + 1
                que.append((cur+1, (r+dr, c+dc)))
                
ans = 0
for di in dist:
    for dij in di:
        ans = max(ans, dij)
print(ans)