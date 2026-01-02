MAX_INT = int(10e10)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

def cnt(c,d):
    if (0 <= c < H) and (0 <= d < W):
        return grid[c][d]
    else:
        return MAX_INT
def tami(a,b):
    num = min(cnt(a+1,b),cnt(a,b+1),cnt(a-1,b),cnt(a,b-1))
    return num+1

H,W = IL()
A = [[i for i in S()] for i in range(H)]

grid = [[MAX_INT]*W for i in range(H)]

for i in range(H):
    for j in range(W):
        if A[i][j] == "#":
            grid[i][j] = 0

for i in range(H):
    for j in range(W):
        if grid[i][j] != 0:
            grid[i][j] = tami(i,j)

for i in range(H-1,-1,-1):
    for j in range(W-1,-1,-1):
        if grid[i][j] != 0:
            grid[i][j] = tami(i,j)

ans = 0
for i in range(H):
    ans = max(ans,max(grid[i][:]))

print(ans)
