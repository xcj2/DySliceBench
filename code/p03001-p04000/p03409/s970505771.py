import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)
from collections import deque

class Dinic:
    def __init__(self,n,edges):
        self.n=n
        self.edges=[[] for _ in range(n)]
        self.iter=[0]*n
        self.level=None
        self.graph(edges)
    def graph(self,E):
        edges=self.edges
        for fr,to,cap in E:
            edges[fr].append([to,cap,len(edges[to])])
            edges[to].append([fr,0,len(edges[fr])-1])
    def maxflow(self,source,sink):
        max_flow=0
        while True:
            self.bfs(source)
            if self.level[sink]<0:
                return max_flow
            self.iter=[0]*self.n
            flow=self.dfs(source,sink,float('inf'))
            while flow:
                max_flow+=flow
                flow=self.dfs(source,sink,float('inf'))
    def bfs(self,source):
        edges=self.edges
        level=[-1]*self.n
        level[source]=0
        q=deque([source])
        while q:
            fr=q.popleft()
            for to,cap,_ in edges[fr]:
                if cap>0>level[to]:
                    level[to]=level[fr]+1
                    q.append(to)
        self.level=level
    def dfs(self,source,sink,flow):
        if source==sink:
            return flow
        while self.iter[source]<len(self.edges[source]):
            to,cap,rev=self.edges[source][self.iter[source]]
            if cap>0 and self.level[source]<self.level[to]:
                f=self.dfs(to,sink,min(flow,cap))
                if f:
                    self.edges[source][self.iter[source]][1]-=f
                    self.edges[to][rev][1]+=f
                    return f
            self.iter[source]+=1
        return 0

def BipartiteMatching(Pairs,a,b):
    Edges=[]
    for x,y in Pairs:
        Edges.append((x+1,a+y+1,1))
    for x in range(a):
        Edges.append((0,x+1,1))
    for y in range(b):
        Edges.append((a+y+1,a+b+1,1))
    solver=Dinic(a+b+2,Edges)
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