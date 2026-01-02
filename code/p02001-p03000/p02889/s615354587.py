import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N,M,L=MI()
    inf=10**15
    d=[[inf]*N for _ in range(N)]
    for i in range(M):
        a,b,c=MI()
        a-=1
        b-=1
        if c<=L:
            d[a][b]=c
            d[b][a]=c
        
    for i in range(N):
        d[i][i]=0
        
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j]=min(d[i][j],d[i][k]+d[k][j])
                
    d2=[[inf]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if d[i][j]<=L:
                d2[i][j]=1
                
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d2[i][j]=min(d2[i][j],d2[i][k]+d2[k][j])
                
    Q=I()
    for i in range(Q):
        s,t=MI()
        s-=1
        t-=1
        ans=d2[s][t]
        if ans>=inf:
            print(-1)
        else:
            print(ans-1)
                
    

main()
