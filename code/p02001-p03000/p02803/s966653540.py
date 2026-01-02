import sys
from collections import deque
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
def input(): return sys.stdin.readline().rstrip()

def main():
    from collections import deque
    dy,dx=[1,0,-1,0],[0,1,0,-1]
    def maze_init(grid,road_chr='.',wall_chr='#',start_chr=None,goal_chr=None):
        H,W=len(grid),len(grid[0])
        if isinstance(grid[0],str):
            grid=[list(row) for row in grid]
        S,G=None,None
        c=[[-1]*(W+2) for _ in range(H+2)]
        for i,row in enumerate(grid,1):
            for j,x in enumerate(row,1):
                if x==road_chr:
                    c[i][j]=0
                elif x==wall_chr:
                    c[i][j]=1
                elif x==start_chr:
                    S=(i,j)
                    c[i][j]=0
                elif x==goal_chr:
                    G=(i,j)
                    c[i][j]=0
        return c,S,G
    def maze_bfs(grid,start_coordinate,road_cost=1,wall_cost=None):
        d=[[INF]*len(grid[0]) for _ in range(len(grid))]
        que=deque()
        que.append((start_coordinate[0],start_coordinate[1]))
        d[start_coordinate[0]][start_coordinate[1]]=0
        while que:
            v=que.popleft()
            for k in range(4):
                nv=(v[0]+dy[k],v[1]+dx[k])
                if grid[nv[0]][nv[1]]==0:
                    if d[nv[0]][nv[1]]>d[v[0]][v[1]]+road_cost:
                        que.append(nv)
                        d[nv[0]][nv[1]]=d[v[0]][v[1]]+road_cost
                elif grid[nv[0]][nv[1]]==1 and wall_cost is not None:
                    if d[nv[0]][nv[1]]>d[v[0]][v[1]]+wall_cost:
                        que.append(nv)
                        d[nv[0]][nv[1]]=d[v[0]][v[1]]+wall_cost
        return d
    
    H,W=map(int,input().split())
    s=[list(input()) for _ in range(H)]
    
    grid,S,G=maze_init(s,road_chr='.',wall_chr='#',start_chr=None,goal_chr=None)
    
    ans=0
    for i in range(1,H+1):
        for j in range(1,W+1):
            d=maze_bfs(grid,(i,j),road_cost=1,wall_cost=None)
            for k in range(1,H+1):
                for l in range(1,W+1):
                    if grid[i][j]==grid[k][l]==0:
                        ans=max(ans,d[k][l])
    print(ans)

if __name__ == '__main__':
    main()
