import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N,K=MI()
    
    #とりあえず重複ありで，個数を数える
    cnt=[0]*(K+1)
    
    for i in range(1,K+1):
        aa=K//i
        cnt[i]=pow(aa,N,mod)
        
    for i in range(K,0,-1):
        pn=-1
        for j in range(2*i,K+1,i):
            #print(i,j,cnt)
            cnt[i]+=cnt[j]*pn
            
    #print(cnt)
    ans=0
    for i in range(1,K+1):
        ans+=(i*cnt[i])%mod
        ans%=mod
        
    print(ans)
    

main()
