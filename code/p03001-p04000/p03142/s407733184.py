import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    """
    書き足した辺は，子孫に対してのものなのでいわゆるショートかっと．
    後から同じ頂点にたどり着いた場合，そちらを優先する？

    """
    
    mod=10**9+7
    N,M=MI()
    fro=[[]for _ in range(N)]
    to=[[]for _ in range(N)]
    
    for _ in range(N+M-1):
        a,b=MI()
        a-=1
        b-=1
        fro[b].append(a)
        to[a].append(b)
        
    root=0
    target=[0]*N
    for i in range(N):
        target[i]=len(fro[i])
        if target[i]==0:
            root=i
        
    P=[-1]*N
    
    #何回通ったかカウント，これがtargetと一致した場合だけ先に進む（最後の一個だけを通すようにする）
    count=[0]*N
    
    import queue
    q=queue.Queue()
    q.put(root)
    
    while not q.empty():
        v=q.get()
        for nv in to[v]:
            count[nv]+=1
            if count[nv]==target[nv]:
                q.put(nv)
                P[nv]=v
                
    for i in range(N):
        print(P[i]+1)
    
        

main()
