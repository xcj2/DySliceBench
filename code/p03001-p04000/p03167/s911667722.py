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
MOD = 10**9+7

grid = []
grid.append("#"*(w+2))
for _ in range(h):
    grid.append("#" + ns() + "#")
grid.append("#"*(w+2))

ans = [[0]*(w+2) for _ in range(h+2)]
ans[1][1] = 1
for i in range(1,h+1):
    for j in range(1,w+1):
        if grid[i][j] == "." and (i,j) != (1,1):
            ans[i][j] = ans[i-1][j] + ans[i][j-1]
            ans[i][j] %= MOD
            
print(ans[h][w])