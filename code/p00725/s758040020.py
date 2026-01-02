import sys
sys.setrecursionlimit(10000000)
MOD = 10 ** 9 + 7
INF = 10 ** 15
Dy = (-1,0,1,0)
Dx = (0,1,0,-1)

MAXH = 25
MAXW = 25
dist = [[100]*MAXW for _ in range(MAXH)]
grid = [[-1]*MAXH for _ in range(MAXH)]

def dfs(ny,nx,t,H,W):
    if t == 11:
        return
    for dy,dx in zip(Dy,Dx):
        y,x = ny,nx
        before_y,before_x = ny,nx
        while True:
            y += dy
            x += dx
            if y < 0 or y >= H:
                break
            if x < 0 or x >= W:
                break
            if grid[y][x] == 1:
                if (before_y,before_x) != (ny,nx):
                    grid[y][x] = 0
                    if dist[before_y][before_x] > t:
                        dist[before_y][before_x] = t
                    dfs(before_y,before_x,t + 1,H,W)
                    grid[y][x] = 1
                break
            if grid[y][x] == 3:
                dist[y][x] = min(t,dist[y][x])
                return
            before_y = y
            before_x = x

def solve(H,W):
    sy,sx,gy,gx = -1,-1,-1,-1
    for i in range(H):
        A = list(map(int,input().split()))
        for j in range(W):
            if A[j] == 2:
                sy,sx = i,j
            if A[j] == 3:
                gy,gx = i,j
            grid[i][j] = A[j]
            dist[i][j] = 100
    
    dist[sy][sx] = 0
    dfs(sy,sx,1,H,W)
    ans = dist[gy][gx] if dist[gy][gx] <= 10 else -1
    print(ans)

def main():
    while True:
        W,H = map(int,input().split())
        if H == 0 and W == 0:
            return
        solve(H,W)
if __name__ == '__main__':
    main()
