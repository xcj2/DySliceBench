import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N,M=MI()
    adj=[[]for _ in range(N)]
    
    for i in range(M):
        a,b=MI()
        a-=1
        b-=1
        adj[a].append(b)
        adj[b].append(a)
        
    import queue
    q=queue.Queue()
    q.put((0,-1))
    ans=[-1]*N
    
    while not q.empty():
        v,p=q.get()
        for nv in adj[v]:
            if nv!=p:
                if ans[nv]==-1:
                    q.put((nv,v))
                    ans[nv]=v
                    
    print("Yes")
    for i in range(1,N):
        print(ans[i]+1)
                

main()
