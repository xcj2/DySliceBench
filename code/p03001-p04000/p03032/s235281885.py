import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N,K=MI()
    V=LI()
    
    ans=0
    import heapq
    
    #左からa個，右からb個とって，あまり分で負数を捨てる
    for a in range(K+1):
        for b in range(K+1):
            if a+b>min(K,N):
                break
            hq=[]
            heapq.heapify(hq)
            for i in range(a):
                heapq.heappush(hq,V[i])
            for j in range(b):
                heapq.heappush(hq,V[N-1-j])
                
            temp=0
            rem=K-(a+b)
            for i in range(a+b):
                v=heapq.heappop(hq)
                if v>=0:
                    temp+=v
                else:
                    if rem>0:
                        rem-=1
                    else:
                        temp+=v
                        
            ans=max(ans,temp)
            
    print(ans)
                
            

main()
