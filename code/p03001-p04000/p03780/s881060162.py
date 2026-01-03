def main():
    def I(): return int(input())
    def MI(): return map(int, input().split())
    def LI(): return list(map(int, input().split()))
    
    N,K=MI()
    a=LI()#下位の連続するn枚が不要なはず
    a.sort()
    for i in range(N):#K以上ならば必要
        if a[i]>=K:
            a=a[:i]
            break
    N=len(a)
                    
                    
    #x番目の数が必要かどうかの判定 
    #必要なものだけで構成された集合をもとに考えれば良いわけではない，不必要な分も考えなければならない             
    def ch(x):
        
        #使い回す，i番目まででjが作れるか
        dp=[0]*K
        dp[0]=1
        for i in range(N):
            if i==x:
                continue
            else:
                for j in range(K-1,a[i]-1,-1):
                    dp[j]|=dp[j-a[i]]
                
                        
        #K未満K-a[x]以上が作れれば良い    
        for j in range(K-a[x],K):
            if  dp[j]:
                return True
        return False
            
    
                        
    ng=-1
    ok=N
    while abs(ok-ng)>1:
        med=(ok+ng)//2
        
        if ch(med):
            ok=med
        else:
            ng=med
            
    print(ng+1)
    
    
 
    

main()
