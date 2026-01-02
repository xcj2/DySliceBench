
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    H,W=MI()
    s=[[] for _ in range(H+2)]
    s[0]="#"*(W+2)
    for i in range(H):
        s[i+1]="#"+input()+"#"
    s[-1]="#"*(W+2)
            
            
    dx=[0,1]
    dy=[1,0]
    
    inf=10**7
    #dp[i][j]はますi,jにたどり着くときの最小コスト，コストは色が変わった数
    dp=[[inf]*(W+2) for _ in range(H+2)]
    
    if s[1][1]==".":
        dp[1][1]=0
    else:
        dp[1][1]=1
        
    for i in range(1,H+1):
        for j in range(1,W+1):
            for k in range(2):
                ii=i+dx[k]
                jj=j+dy[k]
                if s[ii][jj]==s[i][j]:
                    a=0
                else:
                    a=1
                dp[ii][jj]=min(dp[ii][jj],dp[i][j]+a)
    
    print((dp[H][W]+1)//2)
    

main()
