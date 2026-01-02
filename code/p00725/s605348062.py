from collections import deque

def main():

    grid = []
    h,w = 0,0
    y = [1,0,-1,0]
    x = [0,1,0,-1]
    inf = 11
    gy,gx = 0,0
    ans = inf

    def inside(i,j):
        return 0<=i and i<h and 0<=j and j<w 

    def dfs(cy,cx,count):
        nonlocal ans
        if 10<count:return inf
        if ans<=count:return inf
        res = inf
        for i in range(4):
            ny = cy+y[i]
            nx = cx+x[i]
            if not inside(ny,nx):continue
            if grid[ny][nx] == 1:continue
            while True:
                if ny==gy and nx==gx:
                    ans = min(ans,count+1)
                    return count+1
                if not inside(ny+y[i],nx+x[i]):break
                if grid[ny+y[i]][nx+x[i]] == 1:break
                ny += y[i]
                nx += x[i]
            if not inside(ny+y[i],nx+x[i]):continue
            grid[ny+y[i]][nx+x[i]] = 0
            res = min(res,dfs(ny,nx,count+1))
            grid[ny+y[i]][nx+x[i]] = 1
        return res

    while True:
        w,h = map(int,input().split())
        if h == 0:break
        grid = []
        ans = inf
        for _ in range(h):
            grid.append(list(map(int,input().split())))
        sy,sx = 0,0
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 2:
                    grid[i][j] = 0
                    sy,sx = i,j
                if grid[i][j] == 3:
                    grid[i][j] = 0
                    gy,gx = i,j
        res = dfs(sy,sx,0)
        if res == inf:res = -1
        print(res)


if __name__ == '__main__':
    main()

