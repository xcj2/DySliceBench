#!/usr/bin/env pypy3
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N,K=MI()
    a=[[]for _ in range(N)]
    for i in range(N):
        a[i]=LI()
    
    adj=[[]for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if a[i][j]==1:
                adj[i].append(j)
    
        
    M=1
    mm=1
    for i in range(70):
        mm*=2
        M+=1
        if mm>=K:
            break
    
    dab=[[[0]*N for _ in range(N)]for i in range(M)]
    #ダブリング，M回，1~Nの各頂点をスタートして，1~Nそれぞれを終点とする通り数を記憶
    for j in range(N):
        for kk in range(len(adj[j])):
            k=adj[j][kk]
            dab[0][j][k]=1
    
    for i in range(M-1):
        for j in range(N):
            for k in range(N):
                cnt=dab[i][j][k]
                for l in range(N):
                    dab[i+1][j][l]+=cnt*dab[i][k][l]
                    dab[i+1][j][l]%=mod
                    
    ans=[1]*N
    for mm in range(M):#ダブリング
        if K>>mm&1:
            temp=[0]*N
            for i in range(N):#iにいるところから行けるところを探す．
                cnt=ans[i]
                for j in range(N):
                    temp[j]+=dab[mm][i][j]*cnt
                    
            for i in range(N):
                ans[i]=temp[i]
                
    res=0
    for i in range(N):
        res+=ans[i]
        res%=mod
    print(res)
        

main()
