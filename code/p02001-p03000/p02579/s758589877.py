def dfs(x,y,visited,grid,dp,r,c,n):
    stack = [(x,y)]
    k = 0
    while k < len(stack):
        x,y = stack[k]
        if (x,y) not in visited:
            dp[x][y] = n
            visited.add((x,y))
            if x+1 < r and grid[x+1][y] == '.':
                stack.append((x+1,y))

            if y+1 < c and grid[x][y+1] == '.':
                stack.append((x,y+1))

            if x-1 >= 0 and grid[x-1][y] == '.':
                stack.append((x-1,y))

            if y-1 >= 0 and grid[x][y-1] == '.':
                stack.append((x,y-1))

        k += 1

def shortestPath(x,y,edges):
    stack = [(x,0)]
    visited = set()
    k = 0
    while k < len(stack):
        x,d = stack[k]
        if x not in visited:
            visited.add(x)
            if x == y:
                print(d)
                return
            
            for kid in edges[x]:
                stack.append((kid,d+1))

        k += 1

    print(-1)

def main():
    r,c = map(int,input().split())
    x1,y1 = map(int,input().split())
    x2,y2 = map(int,input().split())
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    dp = [[0 for j in range(c)] for i in range(r)]
    grid = []
    for i in range(r):
        grid.append(input())

    visited = set()
    n = 1
    for i in range(r):
        for j in range(c):
            if (i,j) not in visited and grid[i][j] == '.':
                dfs(i,j,visited,grid,dp,r,c,n)
                n += 1

    edges = {}
    for i in range(1,n):
        edges[i] = set()

    for i in range(r):
        for j in range(c):
            if grid[i][j] == '.':
                x = dp[i][j]
                for k in range(max(0,i-2),min(r,i+3)):
                    for l in range(max(0,j-2),min(c,j+3)):
                        y = dp[k][l]
                        if x != y and y != 0:
                            edges[x].add(y)
                            edges[y].add(x)

    x = dp[x1][y1]
    y = dp[x2][y2]
    shortestPath(x,y,edges)

main()
