import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    #各行では連続した区間
    #行ごとに見ないと話が進まん，降りるタイミぐは各列高々3000こ，来るタイミングも同様
    
    mod=10**9+7
    R,C,K=MI()
    S=[[0]*(C+1) for _ in range(R+1)]

    
    for i in range(K):
        r,c,v=MI()
        S[r][c]=v
        
        
    dp1=[[0]*(C+1)for _ in range(R+1)]
    dp2=[[0]*(C+1)for _ in range(R+1)]
    dp3=[[0]*(C+1)for _ in range(R+1)]
    # dp[i][j][k]はi行j列まで見てその行でk個以下
    
    for i in range(R+1):
        for j in range(C+1):
            #S(i,j)からの移動を考える
            
            #右へ移動，-,拾わない，拾う
            if j+1<=C:
                dp1[i][j+1]=max(dp1[i][j+1],dp1[i][j],S[i][j+1])
                dp2[i][j+1]=max(dp2[i][j+1],dp2[i][j],dp1[i][j]+S[i][j+1])
                dp3[i][j+1]=max(dp3[i][j+1],dp3[i][j],dp2[i][j]+S[i][j+1])
            
            #下へ
            if i+1<=R:
                temp=max(dp1[i][j],dp2[i][j],dp3[i][j])
                dp1[i+1][j]=temp+S[i+1][j]
                
    ans=max(dp1[-1][-1],dp2[-1][-1],dp3[-1][-1])
        
    # for i in range(R+1):
    #     print(dp[i])
        
    print(ans)
                
        
    

main()
