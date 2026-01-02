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

h,w = li()
inp = [lc() for _ in range(h)]
grid = [[-1]*w for _ in range(h)]
for i, row in enumerate(inp):
    for j, col in enumerate(row):
        if inp[i][j] == ".":
            grid[i][j] = 0
        else:
            grid[i][j] = 1

dis = [-1, 0, 1, 0]
djs = [0, -1, 0, 1]
hasVisited = [[False]*w for _ in range(h)]

def dfs(sti, stj, h, w):
    stack = [(sti, stj)]
    cnt_white = 0
    cnt_black = 0
    while stack:
        i,j = stack.pop()
        for di, dj in zip(dis, djs):
            if 0 <= i+di < h and 0 <= j+dj < w:
                if (not hasVisited[i+di][j+dj]) and (grid[i+di][j+dj] != grid[i][j]):
                    hasVisited[i+di][j+dj] = True
                    if grid[i+di][j+dj] == 0:
                        cnt_white += 1
                    else:
                        cnt_black += 1
                    stack.append((i+di, j+dj))
               
    return cnt_white * cnt_black

ans = 0
for r in range(h):
    for c in range(w):
        if hasVisited[r][c]:
            continue
        
        cnt = dfs(r,c,h,w)
        ans += cnt
        
print(ans)
        