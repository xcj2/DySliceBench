
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    S=input()
    N=len(S)
    K=I()
    
    dpl=[[0]*(K+1)for _ in range(N+1)]
    dpt=[[0]*(K+1)for _ in range(N+1)]
    
    #dp[i][j]はi桁目まで見て0以外がj個．tは上限
    dpt[0][0]=1
    
    for i in range(N):
        #とりあえずルーズな方
        for j in range(K+1):
            dpl[i+1][j]=dpl[i][j]# 0が増えた場合
            
        for j in range(1,K+1):
            dpl[i+1][j]+=dpl[i][j-1]*9 # 0以外が増えた場合
            
        s=int(S[i])
        #タイトな方
        if s==0:
            for j in range(K+1):
                dpt[i+1][j]=dpt[i][j]#0をつけるしかない
        else:
            for j in range(1,K+1):
                dpt[i+1][j]=dpt[i][j-1]#0以外をつける
            
            #ルーズに落ちる
            for j in range(K+1):
                dpl[i+1][j]+=dpt[i][j]#0をつける
            #ルーズに落ちる
            for j in range(K):
                dpl[i+1][j+1]+=dpt[i][j]*(s-1)#0以外をつける
                
    ans=dpt[-1][-1]+dpl[-1][-1]
    
    print(ans)
    
    # for i in range(N+1):
    #     print(dpt[i])
        
    # print()
    # for i in range(N+1):
    #     print(dpl[i])
                
            
            
        
        

main()
