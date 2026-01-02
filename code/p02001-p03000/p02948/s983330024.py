import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    import heapq
    mod=10**9+7
    N,M=MI()
    L=[[]for _ in range(M)]
    for i in range(N):
        #何日までに受ける必要があるかを気にしながら持つ
        a,b=MI()
        if a<=M:
            L[M-a].append(-b)
        
    ans=0
    hq=[]
    heapq.heapify(hq)
    
    for i in range(M-1,-1,-1):
        for bb in L[i]:
            heapq.heappush(hq,bb)
            
        if len(hq)!=0:
            temp=heapq.heappop(hq)
            ans+=-1*temp
        
    print(ans)
        
        

main()
