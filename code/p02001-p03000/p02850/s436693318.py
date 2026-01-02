import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    P=[-1]*N#親から来た辺の色だけ持っておく
    C=[0]*(N-1)
    adj=[[]for _ in range(N)]
    
    from collections import defaultdict
    dd = defaultdict(lambda : -1)
    dd2 = defaultdict(lambda : -1)
    
    for i in range(N-1):
        a,b=MI()
        a-=1
        b-=1
        adj[a].append(b)
        adj[b].append(a)
        
        dd[(a,b)] = i
        dd2[i]=(a,b)
        
    
    import queue
    q=queue.Queue()
    q.put((0,-1))
    
    while not q.empty():
        v,p=q.get()
        
        col=0
        for i in range(len(adj[v])):
            nv=adj[v][i]
            
            if nv==p:
                continue
            
            if col==P[v]:
                col+=1
            
            a=min(v,nv)
            b=max(v,nv)
            ii=dd[(a,b)]
            C[ii]=col
            P[nv]=col
            col+=1
            
            q.put((nv,v))
            
    K=0
    for i in range(N):
        K=max(K,len(adj[i]))
    
    print(K)
    for i in range(N-1):
        print(C[i]+1)

            
    
    
    

main()
