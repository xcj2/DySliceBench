import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    T=I()
    import heapq
    from collections import defaultdict
    inf=10**18+1
    for _ in range(T):
        #print("---")
        L=[0]*4
        N,L[0],L[1],L[2],L[3]=MI()
        LL=[2,3,5]
        dd = defaultdict(lambda: inf)
        dd[0]=0
        q=[(0,N,1)]#cost，数字，+-1を使えるか
        heapq.heapify(q)
        ans=L[3]*N
        while True:
            cost,now,flag=heapq.heappop(q)
            if now==0:
                ans=cost
                break
            if cost>ans:
                break
            ans=min(ans,cost+now*L[3])
            
            for i in range(3):
                if now%LL[i]==0:
                    nxt=now//LL[i]
                    ncost=cost+L[i]
                    if ncost<dd[nxt]:
                        dd[nxt]=ncost
                        heapq.heappush(q,(ncost,nxt,1))
            
            if flag:
                for k in range(1,5):
                    for pm in [1,-1]:
                        nxt=now+k*pm
                        ncost=cost+L[3]*k
                        if ncost<dd[nxt]:
                            dd[nxt]=ncost
                            heapq.heappush(q,(ncost,nxt,0))
                    
        print(ans)
                
                    
            
        
        
        
        
        
        

main()
