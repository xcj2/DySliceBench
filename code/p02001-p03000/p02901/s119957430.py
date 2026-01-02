import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    import itertools
    
    mod=10**9+7
    N,M=MI()
    a=[0]*M
    b=[0]*M
    c=[]
    
    for i in range(M):
        a[i],b[i]=MI()
        cc=LI()
        for j in range(b[i]):
            cc[j]-=1
        c.append(cc)
        
    N2=pow(2,N)
    inf=10**10
    
    def encode(L):
        temp=0
        for i in range(len(L)):
            temp+=L[i]<<i
        return temp
            
    
    dp=[[inf]*N2 for _ in range(M+1)]
    # i番目の鍵までで状態jを達成できる最小値
    
    dp[0][0]=0
    for i in range(M):
        for ite in itertools.product([0,1], repeat=N):
            L=list(ite)
            j=encode(L)
            for k in c[i]:
                L[k]=1
            nj=encode(L)
            # print(i,ite,j,nj)
            if dp[i][j]!=inf:
                dp[i+1][j]=min(dp[i+1][j], dp[i][j])
                dp[i+1][nj]=min(dp[i+1][nj], dp[i][j]+a[i])
        
    ans=dp[-1][-1]
    if ans==inf:
        ans=-1
    print(ans)
    
    # for i in range(M+1):
    #     print(dp[i])
                
    

main()
