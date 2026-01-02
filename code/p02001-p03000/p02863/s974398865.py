import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

"""
最後に食べるもので場合わけ，最後のもの以外を使う．
[0,i)と(i,N-1]の2つのdpで
"""
def main():
    mod=10**9+7
    N,T=MI()
    A=[0]*N
    B=[0]*N
    for i in range(N):
        A[i],B[i]=MI()
        
    M=3000
    
    def calc(A,B):
        dp=[[0]*(M+1) for _ in range(N+1)]
        for i in range(N):
            a=A[i]
            b=B[i]
            for j in range(1,M+1):
                dp[i+1][j]=max(
                    dp[i+1][j], # ここ
                    dp[i+1][j-1],# 1つまえの時間でも達成できる
                    dp[i][j]# i番目を選ばない
                    )
                if j-a>=0:
                    dp[i+1][j]=max(
                        dp[i+1][j],
                        dp[i][j-a]+b
                    )
        return dp
                
    dp=calc(A,B)
    # dp[i][j]はi番目までみて，j分以内に食べられる最大値
    
    dp2=calc(A[::-1],B[::-1])
    # dp2[i][j]は後ろからi個みて，j分以内に食べられる最大値
    

              
    ans=0
    for i in range(N):
        a=A[i]
        b=B[i]
        temp=0
        for j in range(T):#最後にi番目をオーダーするので，T-1秒の間にどこまでいけるか
            aa=dp[i][j]
            bb=dp2[N-i-1][T-j-1]
            temp=max(temp,aa+bb)
        ans=max(ans,temp+b)
            
        # print(i,a,b,ans)
            
    print(ans)
                
 

main()
