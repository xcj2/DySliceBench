import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    adj=[[]for _ in range(N)]
    for i in range(N-1):
        u,v,w=MI()
        u-=1
        v-=1
        adj[u].append((v,w))
        adj[v].append((u,w))
        
    
    ans=[-1]*N
    import queue
    
    q=queue.Queue()
    q.put(0)
    ans[0]=0
    
    while not q.empty():
        v=q.get()
        for nv,w in adj[v]:
            if ans[nv]==-1:
                if ans[v]==0 and w%2==0:
                    ans[nv]=0
                elif ans[v]==0 and w%2==1:
                    ans[nv]=1
                elif ans[v]==1 and w%2==0:
                    ans[nv]=1
                else:
                    ans[nv]=0
                q.put(nv)
                
    for i in range(N):
        print(ans[i])
    
    

main()
