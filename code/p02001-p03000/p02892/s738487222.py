

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    
    adj=[[]for _ in range(N)]
    
    
    for i in range(N):
        S=list(input())
        for j in range(N):
            if S[j]=="1":
                adj[i].append(j)
            
    import queue
    
    ans=0
    
    
    def bfs(x):
        q=queue.Queue()
        q.put((x,1))
        V=[-1]*N
        V[x]=1
        flag=0
        while not q.empty():
            v,d=q.get()
            for nv in adj[v]:
                if V[nv]==-1:
                    V[nv]=d+1
                    q.put((nv,d+1))
                if abs(V[nv]-V[v])!=1:
                    flag=1
                    break
                
        if flag:
            return -1
        return max(V)
    
    ans=0
    for i in range(N):
        temp=bfs(i)
        if temp==-1:
            ans=-1
            break
        ans=max(ans,temp)
    print(ans)
    
                    

        
        

main()
