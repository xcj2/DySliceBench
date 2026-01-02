import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    
    #0から他の頂点へ
    def BellmanFord(N, M, edges):
        #N頂点，M辺，edgesのリスト
        inf=10**20
        d = [inf] * N
        d[0] = 0

        for i in range(N-1):
            for (u, v, c) in edges:
                if to[u] and to[v] and rto[u] and rto[v]:
                    if d[u] + c < d[v]:
                        d[v] = d[u] + c

        
        #何処かの最短距離がまだ更新されるか確認
        for (u, v, c) in edges:
            if to[u] and to[v] and rto[u] and rto[v]:
                if d[u] + c < d[v]:
                    return None#負の閉路
                
        return d[N-1]
    
    N,M,P=MI()
    edges=[]
    adj1=[[]for _ in range(N)]
    adj2=[[]for _ in range(N)]
    for _ in range(M):
        a,b,c=MI()
        a-=1
        b-=1
        c-=P
        edges.append([a,b,-1*c])
        adj1[a].append(b)
        adj2[b].append(a)
        
    ################
    #BFSで使う点を選択．
    import queue
    q=queue.Queue()
    
    to=[0]*N
    to[0]=1
    rto=[0]*N
    rto[-1]=1
    
    q.put(0)
    while not q.empty():
        v=q.get()
        for nv in adj1[v]:
            if to[nv]==0:
                to[nv]=1
                q.put(nv)
                
    q.put(N-1)
    while not q.empty():
        v=q.get()
        for nv in adj2[v]:
            if rto[nv]==0:
                rto[nv]=1
                q.put(nv)
        
    
    ################
    
    ans=BellmanFord(N,M,edges)
    
    if ans==None:
        print(-1)
    elif ans>=10**10:
        print(-1)
    else:
        print(max(-1*ans,0))
    
        

main()
