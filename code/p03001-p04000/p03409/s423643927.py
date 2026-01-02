from collections import defaultdict
import sys
sys.setrecursionlimit(10**7)

class Ford_Fulkerson:
    def __init__(self,G,N,s,t):
        self.G,self.N,self.s,self.t=G,N,s,t
        self.max_f=self.Max_Flow(self.G,self.s,self.t)
        
    def dfs(self,G,v,t,f,used):
        if v==t:
            return f
        used[v]=True
        for nv,cap in G[v].items():
            if not used[nv] and cap>0:
                d=self.dfs(self.G,nv,t,min(f,cap),used)
                if d>0:
                    self.G[v][nv]-=d
                    self.G[nv][v]+=d
                    return d
        return 0

    def Max_Flow(self,G,s,t):
        flow=0
        while(True):
            used=[False]*(2*N+2)
            f=self.dfs(self.G,self.s,self.t,float('inf'),used)
            if f==0:
                return flow
            flow+=f

N=int(input())
G=[defaultdict(int) for i in range(2*N+2)]
arr=[]
for i in range(2*N):
    x,y=map(int,input().split())
    arr.append((x,y))

for i in range(N,2*N):
    for j in range(N):
        a,b=arr[i]
        c,d=arr[j]
        if a>c and b>d:
            G[i+1][j+1]=1
            G[j+1][i+1]=0
for i in range(1,2*N+1):
    if i>=N+1:
        G[0][i]=1
        G[i][0]=0
    else:
        G[i][2*N+1]=1
        G[2*N+1][i]=0

MF=Ford_Fulkerson(G,2*N+2,0,2*N+1)
print(MF.max_f)