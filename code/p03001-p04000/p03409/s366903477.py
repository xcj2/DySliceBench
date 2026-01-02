import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)

class FordFulkerson:
    def __init__(self,n):
        self.visited=[False]*n
        self.G=[[0]*n for _ in range(n)]
        self.n=n
    def add_edge(self,fr,to,cap):
        self.G[fr][to]=cap
    def dfs(self,start,goal,f):
        if start==goal:
            return f
        self.visited[start]=True
        for i in range(self.n):
            if i==start:
                continue
            if (not self.visited[i]) and self.G[start][i]>0:
                d=self.dfs(i,goal,min(f,self.G[start][i]))
                if d>0:
                    self.G[start][i]-=d
                    self.G[i][start]+=d
                    return d
        return 0
    def maxflow(self,source,sink):
        flow=0
        while True:
            self.visited=[False]*self.n
            f=self.dfs(source,sink,float('inf'))
            if f==0:
                break
            flow+=f
        return flow

def BipartiteMatching(Pairs,a,b):
    solver=FordFulkerson(a+b+2)
    for x,y in Pairs:
        solver.add_edge(x+1,a+y+1,1)
    for x in range(a):
        solver.add_edge(0,x+1,1)
    for y in range(b):
        solver.add_edge(a+y+1,a+b+1,1)
    return solver.maxflow(0,a+b+1)

n=int(input())
R=[list(map(int,input().split())) for _ in range(n)]
B=[list(map(int,input().split())) for _ in range(n)]
Pairs=[]
for i in range(n):
    for j in range(n):
        if R[i][0]<B[j][0] and R[i][1]<B[j][1]:
            Pairs.append((i,j))
print(BipartiteMatching(Pairs,n,n))