import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N,M=MI()
    H=LI()
    adj=[[]for _ in range(N)]
    for i in range(M):
        a,b=MI()
        a-=1
        b-=1
        adj[a].append(b)
        adj[b].append(a)
        
    used=[0]*N
    Hi=[[0,0]for _ in range(N)]
    for i in range(N):
        Hi[i][0]=H[i]
        Hi[i][1]=i
        
    Hi.sort(reverse=True)
    
    ans=0
    for i in range(N):
        v=Hi[i][1]
        HH=Hi[i][0]
        if used[v]==0:
            temph=0
            used[v]=1
            for nv in adj[v]:
                temph=max(H[nv],temph)
                used[nv]=1
            if HH>temph:
                ans+=1
                
    print(ans)
        
    

main()
