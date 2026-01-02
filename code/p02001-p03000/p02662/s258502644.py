import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=998244353
    N,S=MI()
    A=LI()
    dp=[[0]*(S+1) for _ in range(N+1)]
    #dp[i][j]はi番目までで，和がjになるのが何個作れるか．
    #ただし，その数を使わない場合，選択するかしないか選べるのでダブルでカウント
    
    dp[0][0]=1
    
    
    for i in range(N):
        #dp[i][0]+=1
        for j in range(S+1):
            dp[i+1][j]+=dp[i][j]*2
            dp[i+1][j]%=mod
            if j+A[i]<=S:
                dp[i+1][j+A[i]]+=dp[i][j]
                dp[i+1][j+A[i]]%=mod
                
    print(dp[-1][-1])
    

            

main()
