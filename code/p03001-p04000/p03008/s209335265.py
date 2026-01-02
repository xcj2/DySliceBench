import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    A=LI()
    B=LI()
    
    dp=[0]*(N+1)
    #i番目まで見てj個使って何個増やせたか
    
    v=[]
    for i in range(3):
        vv=B[i]-A[i]#差分だけ増える
        v.append(vv)
        
    for i in range(3):
        for j in range(A[i],N+1,1):
            dp[j]=max(dp[j-A[i]]+v[i],dp[j])
            
    N2=N#A=>Bでどこまで増えたか
    for j in range(N+1):
        temp=N+dp[j]
        N2=max(N2,temp)

        
    #B=>A
    dp2=[0]*(N2+1)
    for i in range(3):
        for j in range(B[i],N2+1,1):
            dp2[j]=max(dp2[j-B[i]]-v[i],dp2[j])#価値が逆転
            
    ans=N2
    for j in range(N2+1):
        temp=N2+dp2[j]
        ans=max(ans,temp)
        
    print(ans)
            
  
            

main()
