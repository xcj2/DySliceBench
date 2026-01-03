import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
import copy

def main():
    N,M=MI()
    inf=10**10
    adj=[[inf]*N for _ in range(N)]
    for i in range(N):
        adj[i][i]=0
        
    
    for i in range(M):
        a,b,c=MI()
        a-=1
        b-=1
        adj[a][b]=c
        adj[b][a]=c
        
    d=copy.deepcopy(adj)
    
    def warshall_floyd(d):
            #d[i][j]: iからjへの最短距離
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    d[i][j] = min(d[i][j],d[i][k] + d[k][j])
        return d
    
    ans=0
    d=warshall_floyd(d)
    
    for i in range(N):
        for j in range(N):
            if d[i][j]!=adj[i][j] and adj[i][j]!=inf:
                ans+=1
                
    print(ans//2)
    
        
    
    
        

main()
