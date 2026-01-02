import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    import queue
    N,Q=MI()
    adj=[[]for _ in range(N)]
    for _ in range(N-1):
        a,b=MI()
        a-=1
        b-=1
        adj[a].append(b)
        adj[b].append(a)
        
    ans=[0]*N
    for _ in range(Q):
        p,x=MI()
        p-=1
        ans[p]+=x
        
    q=queue.Queue()
    q.put((0,-1))
    
    while not q.empty():
        v,p=q.get()
        for nv in adj[v]:
            if nv!=p:
                ans[nv]+=ans[v]
                q.put((nv,v))
                
    print(' '.join(map(str, ans)))
        
    

main()
