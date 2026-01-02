import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    T=I()
    import heapq
    
    def calc(X):
        #厳しいところから見ていき，大きいものから入れていく
        hq=[]
        heapq.heapify(hq)
        X.sort(reverse=True)#厳しい順に
        N2=len(X)
        cur=0
        temp=0
        for i in range(N2-1,-1,-1):
            while cur<=N2-1:
                k=X[cur][0]
                if k>i:
                    heapq.heappush(hq,-1*X[cur][1])
                    cur+=1
                else:
                    break
            if len(hq)!=0:
                a=heapq.heappop(hq)
                temp+=-1*a
                
        #print(X,temp)
        return temp 
    
    
    for _ in range(T):
        # 左右それぞれどちらにいきたいかで分けていくことで問題を独立に
        N=I()
        ans=0
        L=[]
        R=[]
        for i in range(N):
            K,l,r=MI()
            if l>=r:
                ans+=r
                L.append((K,l-r))#左からK以内なら+l-r点
            else:
                ans+=l
                R.append((N-K,r-l))#右からN-K以内なら+r-l点
                
        ans+=calc(L)
        ans+=calc(R)
        print(ans)
        
        
        

main()




